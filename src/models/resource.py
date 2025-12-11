from datetime import datetime
from typing import Self
from uuid import uuid4
from pydantic import BaseModel, Field

class Resource(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str = Field(min_length=1, max_length=24)
    url: str
    category: str 
    added_by: str
    added_at: datetime
        
    def __str__(self) -> str:
        return f"Resource: {self.title}, was added by: {self.added_by} "
    
    def format_link(self) -> str:
        return (f"[{self.title}]({self.url})")
    