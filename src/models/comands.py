from pydantic import BaseModel


class SimpleCommand(BaseModel):
    arg: str


class AboutCommand(SimpleCommand):
    comunity: bool = False
