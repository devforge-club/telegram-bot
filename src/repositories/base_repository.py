from bson import ObjectId
from pymongo.asynchronous.database import AsyncDatabase


class BaseRepository:
    
    def __init__(self, db: AsyncDatabase, collection_name: str):
        """
        db: instancia de AsyncDatabase
        collection_name: nombre de la colección
        """
        self.collection = db[collection_name]

