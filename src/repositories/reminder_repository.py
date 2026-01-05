from pymongo.asynchronous.database import AsyncDatabase
from ..models.reminder import Reminder
from datetime import datetime
from base_repository import BaseRepository


class ReminderRepository(BaseRepository):
    def __init__(self, db: AsyncDatabase):
        super().__init__(db, "reminders")

    async def create(self, reminder: Reminder) -> Reminder:
        result = await self.db.insert_one(reminder.model_dump(exclude={"id"}))
        reminder.id = str(result.inserted_id)
        return reminder
    
