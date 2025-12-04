from datetime import datetime
from typing import Self
from uuid import uuid4
class Resource:
    id: str
    title: str
    url: str
    category: str
    added_by: str
    added_at: datetime
    
    def __init__ (self,
                  title: str, 
                  url: str, 
                  category: str, 
                  added_by: str, 
                  added_at: datetime | None = None,
                  id: str | None = None,):
        self.id = id if id else str(uuid4())
        self.title = title
        self.url = url
        self.category = category
        self.added_by = added_by
        self.added_at = added_at if added_at else datetime.now()
    
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
        return cls(id=data["id"], 
                   title=data["title"], 
                   url=data["url"], 
                   category=data["category"], 
                   added_by=data["added_by"], 
                   added_at=datetime.fromisoformat(data["added_at"]))
    
    def format_link(self) -> str:
        return (f"[{self.title}]({self.url})")
    