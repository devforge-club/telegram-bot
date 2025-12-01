from datetime import datetime
from uuid import uuid4


class Reminder:
    id: str
    user_id: str
    chat_id: str
    message: str
    remind_at: datetime
    created_at: datetime

    def __init__(
        self,
        user_id: str,
        message: str,
        remind_at: str,
        chat_id: str | None = None,
        id: str | None = None,
        created_at: str | None = None,
    ) -> None:
        """Clase que representa un recordatorio personal programado

        Args:
            user_id (str): ID del usuario creador
            message (str): Texto del recordatorio
            remind_at (str): Fecha y hora exacta en la que se debe disparar la notificación
            chat_id (str, optional): Si es `None` toma el valor de `user_id`
            id (str, optional): Este valor solo se pasa cuando se construye la clase a partir de un diccionaro. Para instancias nuevas el constructor crea un uuid automaticamente.
            created_at (str, optional): Este valor solo se pasa cuando se construye la clase a partir de un diccionaro. Para instancias nuevas el constructor toma el valor de `datetime.now()`.
        """
        self.id = id if id else str(uuid4())
        self.user_id = user_id
        self.chat_id = chat_id if chat_id else user_id
        self.message = message
        self.remind_at = datetime.fromisoformat(remind_at)
        self.created_at = (
            datetime.fromisoformat(created_at) if created_at else datetime.now()
        )

    def __str__(self) -> str:
        """Retorna un resumen

        Returns:
            str: ej: "Recordatorio para `self.user_id` a las `self.remind_at` con el mensaje: '`self.message`'"
        """
        return f"Recordatorio para {self.user_id} a las {self.remind_at} con el mensaje: '{self.message}'"

    def is_due(self) -> bool:
        """Método auxiliar para que el Job Runner sepa si toca enviar o no.

        Returns:
            bool: Retorna `True` si `datetime.now()` es mayor o igual a `self.remind_at`.
        """
        return datetime.now() >= self.remind_at

    def to_dict(self) -> dict:
        """Devuelve una representación de esta instancia en forma de diccionario

        Returns:
            dict: Diccionario con las claves:
                - "id" (str)
                - "user_id" (str)
                - "chat_id" (str)
                - "message" (str)
                - "remind_at" (str)
                - "created_at" (str)
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "chat_id": self.chat_id,
            "message": self.message,
            "remind_at": self.remind_at.isoformat(),
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Reminder":
        """Devuelve una instancia de la clase a partir de un diccionario

        Args:
            data (dict): Claves requeridas:
                - "id" (str)
                - "user_id" (str)
                - "chat_id" (str)
                - "message" (str)
                - "remind_at" (str)
                - "created_at" (str)


        Returns:
            Reminder: Nueva instancia de la clase
        """
        return cls(
            user_id=data["user_id"],
            message=data["message"],
            remind_at=data["remind_at"],
            chat_id=data["chat_id"],
            id=data["id"],
            created_at=data["created_at"],
        )
