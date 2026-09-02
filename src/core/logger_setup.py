"""Setup de logger simples usado pela aplicação."""
import logging
from pathlib import Path


def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
    # Nível padrão para evitar mensagem duplicada em testes
    logger.setLevel(logging.INFO)
    return logger
