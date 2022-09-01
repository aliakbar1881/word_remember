from src.page.window import render
from src.words import words

render(words())

if __name__ == "__main__":
    from loguru import logger
    logger.info("src/page/__init__.py")
