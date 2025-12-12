from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
import re


class SimpleCommand(BaseModel):
    arg: str


class AboutCommand(SimpleCommand):
    comunity: bool = False


class ResourceCommand(SimpleCommand): ...


class AddResourceCommand(SimpleCommand):
    url: str = Field(..., pattern=r"^https?://[^\s]+$")
    categories: str


class RemindCommand(SimpleCommand):
    at: datetime


class SummonCommand(SimpleCommand):
    description: Optional[str] = None
    date: datetime
    location: Optional[str]


class AnnounceCommand(SimpleCommand):
    to: Optional[str] = None
    topics: Optional[str] = None
