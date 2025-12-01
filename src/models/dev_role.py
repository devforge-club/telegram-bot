from typing import Self

class DevRole:
    key: str
    name: str
    icon: str
    
    def __init__(self, key: str, name: str, icon: str ):
        self.key = key
        self.name = name
        self.icon = icon
        
    def __str__(self) -> str:
        return f"{self.icon} {self.name}"
    
    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "name": self.name,
            "icon": self.icon
        }
        
    
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(**data)
    
class Backend(DevRole):
    def __init__(self):
        super().__init__(
            key = "backend", 
            name = "Backend Developer", 
            icon = "⚙️")
        
class Frontend(DevRole):
    def __init__(self):
        super().__init__(
            key = "frontend", 
            name = "Frontend Developer", 
            icon = "🎨")
        
class Tester(DevRole):
    def __init__(self):
        super().__init__(
            key = "tester", 
            name = "QA Tester", 
            icon = "🧪")
        
class DevOps(DevRole):
    def __init__(self):
        super().__init__(
            key = "devops", 
            name = "DevOps Engineer", 
            icon = "☁️")
        
        
        

        

        

        