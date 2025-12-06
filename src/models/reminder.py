from datetime import datetime
from uuid import uuid4
from typing import Self
from pydantic import BaseModel, Field

class Reminder(BaseModel):
    user_id: str = Field(min_length=1, max_length=24)
    message: str = Field(min_length=1, max_length=48)
    remind_at: str
    chat_id: str = Field(default=user_id)
    id: str = Field(default=uuid4())
    created_at: str = Field(default=datetime.now())

    """Clase que representa un recordatorio personal programado
        Args:
            user_id (str): ID del usuario creador
            message (str): Texto del recordatorio
            remind_at (str): Fecha y hora exacta en la que se debe disparar la notificación
            chat_id (str, optional): Si es `None` toma el valor de `user_id`
            id (str, optional): Este valor solo se pasa cuando se construye la clase a partir de un diccionaro. Para instancias nuevas el constructor crea un uuid automaticamente.
            created_at (str, optional): Este valor solo se pasa cuando se construye la clase a partir de un diccionaro. Para instancias nuevas el constructor toma el valor de `datetime.now()`.
    """

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
    