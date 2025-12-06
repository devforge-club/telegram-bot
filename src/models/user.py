from datetime import datetime
from .record import Record
from .bot_rol import BotRol, Guest
from .dev_role import DevRole
from typing import Self
from pydantic import BaseModel, Field


class User(BaseModel):
    """
    Clase para representar a los usuarios del bot
    """
    
    telegram_id: str = Field(min_length=2, max_length=24)
    username: str = Field(min_length=2, max_length=24)
    name: str = Field(min_length=1, max_lenght=2)
    bot_rol: BotRol 
    record: Record | None
    joined_at: datetime
    dev_rol: DevRole 

    def __str__(self) -> str:
        return f"[<user>: {self.username}, <bot_rol>: {self.bot_rol}, <joined_at>: {self.joined_at}]"

    def have_permission(self, command: str) -> bool:
        """Comprueba si el usuario tiene permiso de ejecutar un comando

        Args:
            command (str): El comando que se desea comprobar

        Returns:
            bool: Devuelve `True` o `False` en dependencia de si el usuario tiene permiso o no
        """
        return self.bot_rol.can_access_command(command)
