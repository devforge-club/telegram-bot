from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    bot_token: str | None = Field(default=None, alias="BOT_TOKEN")
    webhook_secret: str | None = Field(default=None, alias="WEBHOOK_SECRET")
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

print(settings)
