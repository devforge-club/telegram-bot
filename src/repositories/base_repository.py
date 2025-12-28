from bson import ObjectId
from pymongo.asynchronous.database import AsyncDatabase


class BaseRepository:
    
    def __init__(self, db: AsyncDatabase, collection_name: str):
        
        self.collection = db[collection_name]

    def _map_doc(self, doc: dict | None) -> dict | None:
        
        if doc is None:
            return None

        mapped = dict(doc)

        oid = mapped.pop("_id", None)

        if oid is not None:
            mapped["id"] = str(oid)

        return mapped

    def _to_object_id(self, value: str | None) -> ObjectId | None:
        
        if not value:
            return None

        try:
            return ObjectId(value)
        except Exception:
            return None
