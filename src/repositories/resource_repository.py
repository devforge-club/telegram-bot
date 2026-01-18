from pymongo import DESCENDING
from pymongo.asynchronous.database import AsyncDatabase
from src.repositories.base_repository import BaseRepository
from src.models.resource import Resource

class ResourceRepository(BaseRepository):

    def __init__(self, database: AsyncDatabase):
        super().__init__(database, "resources")

    async def create(self, resource: Resource) -> Resource:
        data = resource.model_dump(exclude={"id"})
        result = await self.db.insert_one(data)
        resource.id = str(result.inserted_id)
        return resource
    
    async def delete(self, resource_id: str) -> bool:
        oid = self._to_object_id(resource_id)
        if not oid:
            return False
        result = await self.db.delete_one({"_id": oid})
        return result.deleted_count > 0
    
    async def search(self, query: str) -> list[Resource]:
        cursor = (
            self.db.find(
                {"$text": {"$search": query}},
                {"score": {"$meta": "textScore"}}
            ).sort([("score", {"$meta": "textScore"})])
        )

        results = []
        async for doc in cursor:
            mapped = self._map_doc(doc)
            if mapped:
                results.append(Resource(**mapped))

        return results
    
    async def get_by_category(self, category: str) -> list[Resource]:
        cursor = self.db.find({"category": category})

        results = []
        async for doc in cursor:
            mapped = self._map_doc(doc)
            if mapped:
                results.append(Resource(**mapped))

        return results
    
    async def get_recent(self, limit: int = 5) -> list[Resource]:
        cursor = (
            self.db.find()
            .sort("added_at", DESCENDING)
            .limit(limit)
        )

        results = []
        async for doc in cursor:
            mapped = self._map_doc(doc)
            if mapped:
                results.append(Resource(**mapped))

        return results
    
    
