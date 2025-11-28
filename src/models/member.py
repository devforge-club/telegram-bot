from datetime import datetime
from models import record
from record import Record
from rol import Rol


class Member:
    """
    Clase para representar a los miembros del bot
    """

    telegram_id: str
    username: str
    name: str
    rol: Rol
    status: str
    record: Record | None
    joined_at: datetime

    def __init__(
        self,
        telegram_id: str,
        username: str,
        name: str,
        rol: Rol,
        status: str,
        record: Record | None = None,
        joined_at: datetime | None = None,
    ):
        """Constructor de la clase miembro

        Args:
            telegram_id (str):
            username (str):
            name (str):
            rol (Rol):
            status (str):
            record: (Recoerd):
            joined_at (datetime | None, optional): En caso de ser None se toma el valor de datetime.now(). Defaults to None.
        """
        self.telegram_id = telegram_id
        self.username = username
        self.name = name
        self.rol = rol
        self.status = status
        self.record = record
        self.joined_at = joined_at if joined_at else datetime.now()

    def __str__(self) -> str:
        return self.name

    def to_dict(self) -> dict:
        """Devuelve una representación en forma de diccionario de esta instancia

        Returns:
            dict: Diccionario con las claves:
            - "telegram_id" (str)
            - "username" (str)
            - "name" (str)
            - "rol" (Rol)
            - "status" (str)
            - "record" (Rrecord | None)
            - "joined_at": string en formato ISO
        """
        return {
            "telegram_id": self.telegram_id,
            "username": self.username,
            "name": self.name,
            "rol": self.rol.to_dict(),
            "status": self.status,
            "record": self.record.to_dict() if self.record else None,
            "joined_at": self.joined_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        """Crea una instancia de la clase a partir de un diccionario

        Args:
            data (dict): claves requeridas:
                - "telegram_id" (str)
                - "username" (str)
                - "name" (str)
                - "rol" (Rol)
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
            rol=Rol.from_dict(data["rol"]),
            status=data["status"],
            record=Record.from_dict(data["record"]),
            joined_at=datetime.fromisoformat(data["joined_at"]),
        )
