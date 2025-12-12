from datetime import datetime
from pydantic import BaseModel, HttpUrl
import re


class SimpleCommand(BaseModel):
    arg: str


class AboutCommand(SimpleCommand):
    comunity: bool = False


class ResourceCommand(SimpleCommand): ...


class AddResourceCommand(SimpleCommand):
    url: HttpUrl
    categories: str


class RemindCommand(SimpleCommand):
    at: datetime


class SummonCommand(SimpleCommand):
    description: str | None = None
    date: datetime
    location: str | None = None


class AnnounceCommand(SimpleCommand):
    to: str | None = None
    topics: str | None = None


class WarnCommand(SimpleCommand):
    to: str
