from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from kafka_settings.consumer import consume_requests
from shared.utils import logger
import asyncio


@asynccontextmanager
async def lifespan(_: FastAPI):
    stop_event = asyncio.Event()

    logger.info("FastAPI lifespan: запуск consumer Kafka")
    task = asyncio.create_task(consume_requests(stop_event))

    yield  # Приложение стартовало

    logger.info("FastAPI lifespan: остановка consumer Kafka")
    stop_event.set()
    await task

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
