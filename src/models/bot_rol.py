from src.utils.command_permissions import COMMAND_CONFIG
from pydantic import BaseModel

class BotRol(BaseModel):
    key: str
    name: str
    hierarchy: int
    min_rank_required: int
    
    def __str__(self) -> str:
        return f"Comunity Rol: {self.name}"
    
    def can_access_command(self, command: str) -> bool:
        if command in COMMAND_CONFIG and self.key in COMMAND_CONFIG[command]["roles"]:
            return True
        return False

class Admin(BotRol):
    def __init__(self):
        defaults = {
            "key":"admin", 
            "name":"Admin", 
            "hierarchy":100,
            "min_rank_required":1300
        }
        super().__init__(**defaults)
 
class Member(BotRol):
    def __init__(self):
        defaults = {
                "key":"member", 
                "name":"Membre", 
                "hierarchy":25,
                "min_rank_required":0
        }
        super().__init__(**defaults)


class Guest(BotRol):
    def __init__(self):
        defaults = {
                "key":"guest", 
                "name":"Guest", 
                "hierarchy":1,
                "min_rank_required":0
        }
        super().__init__(**defaults)
    
