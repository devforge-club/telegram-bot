from datetime import datetime
class Resource():
    id: int
    title: str
    url: str
    category: str
    added_by: str
    added_at: datetime
    
    def __init__ (self, id, title, url, category, added_by, added_at = None):
        self.id = id
        self.title = title
        self.url = url
        self.category = added_by
        if self.added_at == None:
            self.added_at = datetime.now()
        else:
            self.added_at = added_at
    
    def __str__(self) -> str:
        return self.title
    
    def to_dict() -> dict:
        pass
        
    def from_dict(cls, data: dict) -> Resource:
        pass
    
    def format_link(self) -> str:
        return (f"[{self.title()}]({self.url})")