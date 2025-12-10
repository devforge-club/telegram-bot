# Comandos a soportar:
# "start", "ayuda", "sobre"
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import random

from src.utils.bot_phrases import START_PHRASES

router = Router()


# Para manejar el /start de usuarios individuales


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(random.choice(START_PHRASES))

