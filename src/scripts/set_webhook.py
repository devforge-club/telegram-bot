import asyncio
from src.bot.dispatcher import bot
from src.core.config import settings

async def main():
    await bot.set_webhook(
        url=f"{settings.domain_url}/webhook",
        secret_token=settings.webhook_secret,
        drop_pending_updates=True 
    )
    info = await bot.get_webhook_info()
    print(f"Webhook configurado: {info.url}")
    
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())