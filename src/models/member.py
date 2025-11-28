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
    
    def to_dict(self) -> dict:
        return {
            "telegram_id": self.telegram_id,
            "username": self.username,
            "name": self.name,
            "joined_at": self.joined_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        return Member(
                    telegram_id=data["telegram_id"],
                    username=data["username"],
                    name=data["name"],
                    joined_at=data["joined_at"],
                    )
