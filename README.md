# 🎨 Coloring Service

Сервис, который принимает **текстовый промпт** или **изображение**, и генерирует **раскраску** с помощью нейросети **Stable Diffusion**.

> ⚠️ **Важно:** данный сервис — **часть распределённой системы** и **не работает автономно**.
> Для полноценной генерации необходимо запустить Telegram-бота, доступного по ссылке:
> 👉 [Lxg1c/botColoringCreator](https://github.com/Lxg1c/botColoringCreator)

---

## 📦 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/Lxg1c/apiColoringCreator.git
cd apiColoringCreator
```

---

### 2. Установка зависимостей (локальный запуск)

> ✅ **Рекомендуется использовать [`Poetry`](https://python-poetry.org/) для управления зависимостями**

Создайте и активируйте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate       # для Linux/macOS
# .\venv\Scripts\activate       # для Windows
```

Установите Poetry (если ещё не установлен):

```bash
pip install poetry
```

Установите зависимости проекта:

```bash
poetry install
```

---

## ⚙️ Технологии и инструменты

* 🧠 **[Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5)** — генерация изображений
* 🚀 **FastAPI** — backend фреймворк для обработки задач
* 🧵 **Kafka** — брокер сообщений для связи с ботом
* 🌍 **Googletrans** — автоматический перевод пользовательских промптов

---