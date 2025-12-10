from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    bot_token: str | None = Field(default=None, alias="BOT_TOKEN")
    webhook_secret: str | None = Field(default=None, alias="WEBHOOK_SECRET")
    group_id: str | None = Field(default=None, alias="GROUP_ID")
    welcome_topic_id: str | None = Field(default=None, alias="WELCOME_TOPIC_ID")
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

print(settings)
