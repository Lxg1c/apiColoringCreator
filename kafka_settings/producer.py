import base64
from aiokafka import AIOKafkaProducer
import json
from shared.utils import logger


async def send_result_to_bot(chat_id: int, user_id: int, image_bytes: bytes):
    logger.info(f"Результат отправлен в топик drawing-result для user_id={user_id}")
    producer = AIOKafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )
    await producer.start()

    try:
        await producer.send("drawing-result", value={
            "chat_id": chat_id,
            "user_id": user_id,
            "image": base64.b64encode(image_bytes).decode('utf-8')
        })
    finally:
        await producer.stop()