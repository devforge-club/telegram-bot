from pydantic import BaseModel

class SimpleCommand(BaseModel):
    arg: str

