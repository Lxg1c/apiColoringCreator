import numpy as np
import cv2
from PIL import Image
import io

def to_coloring_book(image: Image.Image) -> Image.Image:
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(img, 100, 200)
    edges = cv2.bitwise_not(edges)
    return Image.fromarray(edges)

def image_to_bytes(image: Image.Image) -> bytes:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=True)
    buffer.seek(0)
    return buffer.getvalue()
