from datetime import datetime
from uuid import uuid4
from typing import Self
from pydantic import BaseModel, Field, model_validator

class Reminder(BaseModel):
    user_id: str = Field(min_length=1, max_length=24)
    message: str = Field(min_length=1)
    remind_at: datetime
    chat_id: str | None = None
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    
    @model_validator(mode='after')
    def set_default_chat_id(self):
        if self.chat_id is None:
            self.chat_id = self.user_id
        return self

    """Class that represents a scheduled personal reminder
        Args:
        user_id (str): ID of the user who created it
        message (str): Reminder text
        remind_at (str): Exact date and time when the notification should be triggered
        chat_id (str, optional): If `None`, it takes the value of `user_id`
        id (str, optional): This value is only passed when building the class from a dictionary. For new instances, the constructor automatically creates a UUID.
        created_at (str, optional): This value is only passed when building the class from a dictionary. For new instances, the constructor takes the value of `datetime.now()`. 
    """

    def __str__(self) -> str:
        return f"Scheduled reminder for  {self.remind_at} with the message: '{self.message}'"

    def is_due(self) -> bool:
        return datetime.now() >= self.remind_at
    