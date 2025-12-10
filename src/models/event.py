from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field

days = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
    ]

months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
        

class Event(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str = Field(min_length=8, max_length=64)
    description: str = Field(min_length=24, max_length=256)
    date: datetime
    location: str = Field(min_length=8)
    
    def __str__(self)-> str:
        return f"📍{self.title}, {self.date}, {self.location}"
    
    def is_upcoming(self)-> bool:
        return self.date > datetime.now()
    
    def format_date(self) -> str:
        
        day = days[self.date.weekday()]
        month = months[self.date.month - 1]
        
        return self.date.strftime(f"{day} %d de {month}, %I:%M %p")
        