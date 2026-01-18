from pymongo import DESCENDING
from base_repository import BaseRepository
from src.models.resource import Resource

class ResourceRepository(BaseRepository):

    def __init__(self, database):
        super().__init__(database, "resources")

    async def create(self, resource: Resource) -> Resource:
        data = resource.model_dump(exclude={"id"})
        result = await self.db.insert_one(data)
        resource.id = str(result.inserted_id)
        return resource