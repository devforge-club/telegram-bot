from datetime import datetime
from pymongo import DESCENDING
from pymongo.asynchronous.database import AsyncDatabase
from .base_repository import BaseRepository
from src.models.score_logs import ScoreLog


class ScoreLogRepository(BaseRepository):

    def __init__(self, database: AsyncDatabase):
        super().__init__(database, "score_logs")
        
async def create(self, log: ScoreLog) -> ScoreLog:
        log_dict = log.model_dump(exclude={"id"})
        
        result = await self.db.insert_one(log_dict)

        log.id = str(result.inserted_id)

        return log