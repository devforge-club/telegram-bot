from datetime import datetime
from pydantic import BaseModel, HttpUrl, field_validator

from src.utils.resource_categories import RESOURCE_CATEGORIES


class SimpleCommand(BaseModel):
    arg: str


class AboutCommand(SimpleCommand):
    comunity: bool = False


class ResourceCommand(SimpleCommand):
    category: str | None = None

    @field_validator("category")
    def validate_category(cls, cat: str | None) -> None | str:
        if cat is None:
            return cat
        if cat not in RESOURCE_CATEGORIES:
            raise ValueError(
                f"Invalid category '{cat}'. Allowed values are: {', '.join(RESOURCE_CATEGORIES)}"
            )
        return cat


class AddResourceCommand(SimpleCommand):
    url: HttpUrl
    categories: set[str]

    @field_validator("categories", mode="before")
    def validate_categories(cls, cats: str) -> set[str]:
        if isinstance(cats, str):
            return {c.strip() for c in cats.split(",") if c.strip()}
        return cats


class RemindCommand(SimpleCommand):
    at: datetime


class SummonCommand(SimpleCommand):
    description: str | None = None
    date: datetime
    location: str | None = None


class AnnounceCommand(SimpleCommand):
    to: str | None = None
    topics: set[str]

    @field_validator("topics", mode="before")
    def validate_categories(cls, tops: str) -> set[str]:
        if isinstance(tops, str):
            return {t.strip() for t in tops.split(",") if t.strip()}
        return tops


class WarnCommand(SimpleCommand):
    to: str
