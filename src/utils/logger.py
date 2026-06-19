import logging
from logging.handlers import RotatingFileHandler
from config import LOG_DIR


def get_logger(nome: str) -> logging.Logger:
    logger = logging.getLogger(nome)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        file_handler = RotatingFileHandler(
            LOG_DIR / "pipeline.log",
            maxBytes=1_500_000,
            backupCount=8,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        
        console_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.propagate=False
    
    return logger

