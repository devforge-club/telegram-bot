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
    
    def to_dict(self) -> dict:
        data = {
                "id": self.id,
                "title": self.title,
                "url": self.url,
                "category": self.category,
                "added_by": self.added_by,
                "added_at": self.added_at.isoformat()
                }
        return data
    
    @classmethod    
    def from_dict(cls, data: dict) -> Resource:
        dato: Resource
        dato = cls(data["id"], 
                   data["title"], 
                   data["url"], 
                   data["category"], 
                   data["added_by"], 
                   datetime.fromisoformat(data["added_at"]))
        return dato
    
    def format_link(self) -> str:
        return (f"[{self.title()}]({self.url})")