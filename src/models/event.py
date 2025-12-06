from datetime import datetime
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
    id: int = Field(gt=0, le=1024)
    title: str = Field(min_length=8, max_length=64)
    description: str = Field(min_length=24, max_length=256)
    date: datetime
    location: str = Field(min_length=8)
    
    def __str__(self)-> str:
        return f"<event>: {self.title}, <id>: {self.id}, <date;location>: {self.date};{self.location}"
    
    def is_upcoming(self)-> bool:
        return self.date > datetime.now()
    
    def format_date(self) -> str:
        
        day = days[self.date.weekday()]
        month = months[self.date.month - 1]
        
        return self.date.strftime(f"{day} %d de {month}, %I:%M %p")
        