import os
import torch
from diffusers import StableDiffusionPipeline
from config import HF_MODEL_ID, HF_HOME

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "true"
os.environ["HF_HOME"] = HF_HOME

pipe = StableDiffusionPipeline.from_pretrained(
    HF_MODEL_ID,
    use_safetensors=True,
    low_cpu_mem_usage=True
)
pipe.enable_attention_slicing()
pipe.to("cuda" if torch.cuda.is_available() else "cpu")
