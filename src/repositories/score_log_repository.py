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
    
    async def get_by_user(
        self,
        telegram_id: str,
        limit: int = 10,
        skip: int = 0
        ) -> list[ScoreLog]:

        cursor = self.db.find(
            {"user_telegram_id": telegram_id}
        ).sort("timestamp", DESCENDING).skip(skip).limit(limit)

        
        docs = []
        async for doc in cursor:
            mapped = self._map_doc(doc)
            if mapped is None:
                continue
            docs.append(ScoreLog(**mapped))

        return docs
