FROM python:3.13-slim AS build

WORKDIR /app

# 1. Устанавливаем системные зависимости для PyTorch (CUDA не требуется для CPU-версии)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*



RUN pip install --no-cache-dir \
     torch torchvision torchaudio \
     --index-url https://download.pytorch.org/whl/cu118

# 3. Копируем и устанавливаем остальные зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]