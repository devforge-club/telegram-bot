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
        self.id = id if id else str(uuid4())
        self.user_id = user_id
        self.chat_id = chat_id if chat_id else user_id
        self.message = message
        self.remind_at = datetime.fromisoformat(remind_at)
        self.created_at = (
            datetime.fromisoformat(created_at) if created_at else datetime.now()
        )


