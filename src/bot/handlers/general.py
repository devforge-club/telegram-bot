# Comandos a soportar:
# "start", "help", "about"
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import random

from src.utils.bot_phrases import START_PHRASES

router = Router()


# Para manejar el /start de usuarios individuales


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(random.choice(START_PHRASES))
