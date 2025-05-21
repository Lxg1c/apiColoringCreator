# Берем за основу slim версию питона 3.13
FROM python:3.13-slim AS build

# Устанавливаем рабочую папку, название может быть любое
WORKDIR /app

# Устанавливаем системные зависимости для OpenCV и других библиотек
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Устанавлием poetry
RUN pip install poetry

# Копируем poetry.toml и poetry.lock в контейнер
COPY pyproject.toml poetry.lock ./

# Настроим poetry чтобы не создавать виртуальное окружение
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости
RUN poetry install --no-interaction --no-root

# Копируем весь проект в контейнер
COPY . .

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]