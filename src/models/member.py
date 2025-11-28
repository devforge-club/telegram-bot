from datetime import datetime

class Member:
    telegram_id: int
    username: str
    name: str
    joined_at: datetime
    
    def __init__(self, telegram_id, username, name, joined_at=None):
        self.telegram_id = telegram_id
        self.username = username
        self.name = name
        self.joined_at = joined_at if joined_at else datetime.now()

    def __str__(self) -> str:
        return self.name