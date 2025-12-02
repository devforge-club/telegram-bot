from datetime import datetime
from .record import Record
from .bot_rol import BotRol
from .dev_role import DevRole
from typing import Self


class Member:
    """
    Clase para representar a los miembros del bot
    """

    telegram_id: str
    username: str
    name: str
    bot_rol: BotRol
    status: str
    record: Record | None
    joined_at: datetime
    dev_rol: DevRole 

    def __init__(
        self,
        telegram_id: str,
        username: str,
        name: str,
        bot_rol: BotRol,
        status: str,
        record: Record | None = None,
        joined_at: datetime | None = None,
        dev_rol: DevRole | None = None,
    ):
        """Constructor de la clase miembro

        Args:
            telegram_id (str):
            username (str):
            name (str):
            bot_rol (BotRol):
            status (str):
            record: (Record):
            joined_at (datetime | None, optional): En caso de ser None se toma el valor de datetime.now(). Defaults to None.
            dev_rol: (DevRole):
        """
        self.telegram_id = telegram_id
        self.username = username
        self.name = name
        self.bot_rol = bot_rol
        self.status = status
        self.record = record
        self.joined_at = joined_at if joined_at else datetime.now()
        self.dev_rol = dev_rol

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> dict:
        """Devuelve una representación en forma de diccionario de esta instancia

        Returns:
            dict: Diccionario con las claves:
            - "telegram_id" (str)
            - "username" (str)
            - "name" (str)
            - "bot_rol" (BotRol)
            - "status" (str)
            - "record" (Record | None)
            - "joined_at": string en formato ISO
        """
        return {
            "telegram_id": self.telegram_id,
            "username": self.username,
            "name": self.name,
            "bot_rol": self.bot_rol.to_dict(),
            "status": self.status,
            "record": self.record.to_dict() if self.record else None,
            "joined_at": self.joined_at.isoformat(),
            "dev_rol": self.dev_rol.to_dict() if self.dev_rol else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Crea una instancia de la clase a partir de un diccionario

        Args:
            data (dict): claves requeridas:
                - "telegram_id" (str)
                - "username" (str)
                - "name" (str)
                - "bot_rol" (BotRol)
                - "status" (str)
                - "record" (Record | None)
                - "joined_at": string en formato ISO


        Returns:
            Member: nueva instancia de la clase
        """
        return cls(
            telegram_id=data["telegram_id"],
            username=data["username"],
            name=data["name"],
            bot_rol=BotRol.from_dict(data["bot_rol"]),
            status=data["status"],
            record=Record.from_dict(data["record"]) if data["record"] else None,
            joined_at=datetime.fromisoformat(data["joined_at"]),
            dev_rol=DevRole.from_dict(data["dev_rol"]) if data["dev_rol"] else None,
        )

    def have_permission(self, command: str) -> bool:
        """Comprueba si el miembro tiene permiso de ejecutar un comando

        Args:
            command (str): El comando que se desea comprobar

        Returns:
            bool: Devuelve `True` o `False` en dependencia de si el miembro tiene permiso o no
        """
        return self.bot_rol.can_access_command(command)
