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

    
