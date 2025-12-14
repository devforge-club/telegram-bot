from datetime import datetime
from .record import Record
from .bot_rol import BotRol, Guest
from .dev_role import DevRole
from typing import Self
from pydantic import BaseModel, Field, model_validator


class User(BaseModel):
    """
    Class to represent the bot's users
    """
    
    telegram_id: str = Field(min_length=2, max_length=24)
    username: str = Field(min_length=2, max_length=24)
    name: str = Field(min_length=1, max_length=50)
    bot_rol: BotRol 
    record: Record | None
    joined_at: datetime
    dev_rol: DevRole 

    @model_validator(mode='after')
    def set_default_record(self):
        self.record = Record() if not isinstance(self.bot_rol, Guest) else None
        return self


    def __str__(self) -> str:
        return f"Name: {self.name}\n Username: {self.username}\n {self.bot_rol}\n Joined in: {self.joined_at}"

    def have_permission(self, command: str) -> bool:
        """Check if the user has permission to execute a command

            Args:
            command (str): The command you want to check

            Returns:
            bool: Returns `True` or `False` depending on whether the user has permission or not
        """
        return self.bot_rol.can_access_command(command)
