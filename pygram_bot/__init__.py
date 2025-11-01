"""
PyGram Bot — oddiy Telegram bot framework.
"""

from .core import Bot
from .utils import logger
from .exceptions import BotError

__version__ = "0.1.0"
__all__ = ["Bot", "logger", "BotError"]
