from pymongo import DESCENDING
from base_repository import BaseRepository
from src.models.resource import Resource

class ResourceRepository(BaseRepository):

    def __init__(self, database):
        super().__init__(database, "resources")
