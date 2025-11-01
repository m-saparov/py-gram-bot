import logging

logger = logging.getLogger("pygram_bot")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def debug(msg: str):
    logger.debug(msg)
