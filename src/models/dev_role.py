from typing import Self
from pydantic import BaseModel

class DevRole(BaseModel):
    key: str
    name: str
    icon: str
    
    def __str__(self) -> str:
        return f"Team Rol: {self.name} {self.icon}"

class Backend(DevRole):
    def __init__(self):
        defaults = {
            "key":"backend",
            "name":"Backend Developer",
            "icon":"⚙️"
            
        }
        super().__init__(**defaults)
            
class Frontend(DevRole):
    def __init__(self):
        defaults = {
            "key":"frontend",
            "name":"Frontend Developer",
            "icon":"🎨"
                     
        }
        super().__init__(**defaults)
            

class Tester(DevRole):
    def __init__(self):
        defaults = {
            "key":"tester",
            "name":"QA Tester",
            "icon":"🧪"
            
        }
        super().__init__(**defaults)    
            
        
class DevOps(DevRole):
    def __init__(self):
        defaults = {
            "key":"devops",
            "name":"DevOps Engineer",
            "icon":"☁️"
                
        }
        super().__init__(**defaults)
        
        

        

        

        