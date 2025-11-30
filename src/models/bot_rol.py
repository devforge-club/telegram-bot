from src.logic.commands import parse_command
from src.utils.command_permissions import COMMAND_ALLOWLIST

class BotRol:
    key: str
    name: str
    hierarchy: int
    min_rank_required: int

    def __init__(self, key: str, name: str, hierarchy: int, min_rank_required: int) -> None:
        self.key = key
        self.name = name
        self.hierarchy = hierarchy
    
    def __str__(self) -> str:
        return self.name
    
    def can_access_command(self, command: str) -> bool:
        comm = parse_command(command)[0]
        print(comm)
        if comm in COMMAND_ALLOWLIST and self.key in COMMAND_ALLOWLIST[comm]:
            return True
        
        return False

    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "name": self.name,
            "hierarchy": self.hierarchy,
            "min_rank_required": self.min_rank_required
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "BotRol":
        
        return cls(
            key=data["key"],
            name=data["name"],
            hierarchy=data["hierarchy"],
            min_rank_required=data["min_rank_required"]
        )

class Admin(BotRol):

    def __init__(self, hierarchy: int = 100) -> None:
        super().__init__(
            key="admin", 
            name="Administrador", 
            hierarchy=hierarchy,
            min_rank_required=1300
            )
        
class Member(BotRol):

    def __init__(self, hierarchy: int = 25) -> None:
        super().__init__(
            key="member", 
            name="Miembro", 
            hierarchy=hierarchy,
            min_rank_required=0)

class Guest(BotRol):

    def __init__(self) -> None:
        super().__init__(
            key="guest", 
            name="Invitado", 
            hierarchy=1,
            min_rank_required=0)