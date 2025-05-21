import asyncio
from aiokafka import AIOKafkaConsumer
import json
from kafka_settings.producer import send_result_to_bot
from services.generator import handle_prompt, handle_image
from shared.utils import logger


async def consume_requests(stop_event: asyncio.Event):
    consumer = AIOKafkaConsumer(
        'drawing-prompt',
        'drawing-image',
        bootstrap_servers='kafka:9092',
        group_id='api-service',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        session_timeout_ms = 45000,
        heartbeat_interval_ms = 15000,
        max_poll_interval_ms = 600000
    )

    await consumer.start()
    logger.info("Kafka consumer запущен")
    try:
        async for msg in consumer:
            if stop_event.is_set():
                break
            try:
                data = msg.value
                if msg.topic == 'drawing-prompt':
                    result = await handle_prompt(data['prompt'])
                    await send_result_to_bot(data['chat_id'], data['user_id'], result)
                elif msg.topic == 'drawing-image':
                    result = await handle_image(data['image'])
                    await send_result_to_bot(data['chat_id'], data['user_id'], result)
            except Exception as e:
                logger.error(f"Ошибка обработки сообщения: {e}")
    finally:
        logger.info("Останавливаем Kafka consumer...")
        await consumer.stop()
