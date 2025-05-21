import logging
import base64
import io
import torch
from PIL import Image
from diffusers import StableDiffusionPipeline
from services.image_utils import to_coloring_book
from shared.utils import translator

# Инициализация Stable Diffusion
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, use_safetensors=True, low_cpu_mem_usage=True
)
pipe.enable_attention_slicing()
pipe.to("cuda" if torch.cuda.is_available() else "cpu")


async def handle_prompt(user_text: str) -> bytes | None:
    try:
        translated_text = translator.translate(user_text, dest="en")
    except Exception as e:
        logging.error(f"Ошибка перевода: {e}")
        return None

    prompt = f"{translated_text}, black and white line art, coloring book style, clean outlines, simple design, highly detailed, no shading, no patterns, no abstract elements"
    negative_prompt = (
        "abstract, patterns, noise, blurry, low detail, grayscale, shadows, textures"
    )

    try:
        image = pipe(
            prompt,
            negative_prompt=negative_prompt,
            height=512,
            width=512,
            num_inference_steps=50,
            guidance_scale=7.5,
        ).images[0]

        coloring_image = to_coloring_book(image)
        buffer = io.BytesIO()
        coloring_image.save(buffer, format="PNG", optimize=True, quality=95)
        buffer.seek(0)
        return buffer.getvalue()

    except Exception as e:
        logging.error(f"Ошибка генерации: {e}")
        return None


async def handle_image(photo_base64: str) -> bytes:
    try:
        # Декодируем base64 в байты и оборачиваем в BytesIO
        image_data = base64.b64decode(photo_base64)
        image = Image.open(io.BytesIO(image_data))

        if image.mode != "RGB":
            image = image.convert("RGB")
        coloring_image = to_coloring_book(image)

        buffer = io.BytesIO()
        coloring_image.save(buffer, format="PNG", optimize=True)
        buffer.seek(0)
        return buffer.getvalue()

    except Exception as e:
        logging.error(f"Ошибка обработки фото: {e}")
        raise
