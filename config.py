import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
KAFKA_INPUT_TOPIC = "drawing-prompt"
KAFKA_OUTPUT_TOPIC = "drawing-result"
KAFKA_GROUP_ID = "coloring-service"

HF_MODEL_ID = "runwayml/stable-diffusion-v1-5"
HF_HOME = "./huggingface_cache"
