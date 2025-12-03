from datetime import datetime
from typing import Self
import uuid
class Resource:
    id: uuid
    title: str
    url: str
    category: str
    added_by: str
    added_at: datetime
    
    def __init__ (self, title, url, category, added_by, added_at = None):
        self.id = str(uuid.uuid4)
        self.title = title
        self.url = url
        self.category = added_by
        self.added_at = added_at if added_at is not None else datetime.now()
    
    def __str__(self) -> str:
        return self.title
    
    def to_dict(self) -> dict:
        return {
                "id": self.id,
                "title": self.title,
                "url": self.url,
                "category": self.category,
                "added_by": self.added_by,
                "added_at": self.added_at.isoformat()
                }
    
    @classmethod    
    def from_dict(cls, data: dict) -> Self:
        return cls(data["id"], 
                   data["title"], 
                   data["url"], 
                   data["category"], 
                   data["added_by"], 
                   datetime.fromisoformat(data["added_at"]))
    
    def format_link(self) -> str:
        return (f"[{self.title}]({self.url})")
    