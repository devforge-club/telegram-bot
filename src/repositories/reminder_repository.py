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

    async def get_due_reminders(self) -> list[Reminder]:
        docs = await self.db.find({"remind_at": {"$lte": datetime.now()}}).to_list(
            length=100
        )
        return [Reminder(**self._map_doc(doc)) for doc in docs]

    async def delete(self, reminder_id: str) -> bool:
        oid = self._to_object_id(reminder_id)
        if oid:
            result = await self.db.delete_one({"_id": oid})
            return result.deleted_count == 1
        return False

    async def get_by_user(self, telegram_id: str) -> list[Reminder]:
        docs = await self.db.find({"user_id": telegram_id}).to_list(length=100)
        return [Reminder(**self._map_doc(doc)) for doc in docs]
