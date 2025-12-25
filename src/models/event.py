from datetime import datetime
from pydantic import BaseModel, Field

days = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
    ]

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]
        

class Event(BaseModel):
    id: str | None = None
    title: str = Field(min_length=8, max_length=64)
    description: str = Field(min_length=24, max_length=256)
    date: datetime
    location: str = Field(min_length=8)
    
    def __str__(self)-> str:
        return f"📍Event: {self.title}, {self.date}, {self.location}\n\nDescription: {self.description}"
    
    def is_upcoming(self)-> bool:
        return self.date > datetime.now()
    
    def format_date(self) -> str:
        
        day = days[self.date.weekday()]
        month = months[self.date.month - 1]
        
        return self.date.strftime(f"{day} %d de {month}, %I:%M %p")
        