import logging
from deep_translator import GoogleTranslator

# Инициализация переводчика
translator = GoogleTranslator()

# Инициализация логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Добавляем обработчик, если его еще нет (чтобы не дублировать)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
