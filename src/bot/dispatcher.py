from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.core.config import settings
from src.bot.handlers import general

dispatcher = Dispatcher()
dispatcher.include_router(router=general.router)
bot = Bot(
    token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
