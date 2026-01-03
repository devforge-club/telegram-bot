from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    bot_token: str = Field(alias="BOT_TOKEN")
    domain_url: str = Field(alias="DOMAIN_URL")
    webhook_secret: str = Field(alias="WEBHOOK_SECRET")
    group_id: str = Field(alias="GROUP_ID")
    welcome_topic_id: str = Field(alias="WELCOME_TOPIC_ID")
    admin_secret: str= Field(alias="ADMIN_SECRET")
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
