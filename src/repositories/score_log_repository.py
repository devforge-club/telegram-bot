from datetime import datetime
from pymongo import DESCENDING
from pymongo.asynchronous.database import AsyncDatabase
from .base_repository import BaseRepository
from src.models.score_logs import ScoreLog


class ScoreLogRepository(BaseRepository):

    def __init__(self, database: AsyncDatabase):
        super().__init__(database, "score_logs")