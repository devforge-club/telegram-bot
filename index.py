from fastapi import FastAPI, Request, HTTPException
from aiogram.types import Update

from src.bot.dispatcher import bot, dispatcher
from src.core.config import settings

app = FastAPI(title="Main App")


@app.get("/")
async def get_status():
    return {"status": "OK"}


@app.post("/webhook")
async def webhook(request: Request):
    secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
    if secret != settings.webhook_secret:
        raise HTTPException(status_code=403, detail="Forbidden")

    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await   dispatcher.feed_update(bot=bot, update=update)

    return {"ok": True}
