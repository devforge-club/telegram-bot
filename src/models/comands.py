from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
import re


class SimpleCommand(BaseModel):
    arg: str


class AboutCommand(SimpleCommand):
    comunity: bool = False


class ResourceCommand(SimpleCommand): ...
