from pymongo.asynchronous.database import AsyncDatabase
from pymongo import ASCENDING
from ..models.event import Event
from datetime import datetime
from base_repository import BaseRepository


class EventRepository(BaseRepository):
    def __init__(self, db: AsyncDatabase):
        super().__init__(db, "events")

    async def create(self, event: Event) -> Event:

        result = await self.db.insert_one(event.model_dump(exclude={"id"}))

        event.id = str(result.inserted_id)

        return event

    async def get_upcoming(self, limit: int = 5) -> list[Event]:
        docs = (
            await self.db.find({"date": {"$gte": datetime.now()}})
            .limit(limit)
            .sort("date", ASCENDING)
            .to_list()
        )
        return [Event(**self._map_doc(doc)) for doc in docs]

    async def delete(self, event_id: str) -> bool:
        oid = self._to_object_id(event_id)
        if oid:
            result = await self.db.delete_one({"_id": oid})
            return result.deleted_count == 1
        return False

    async def get_all(self)->list[Event]:
      docs = await self.db.find().sort("date", ASCENDING).to_list()
      return [Event(**self._map_doc(doc)) for doc in docs]