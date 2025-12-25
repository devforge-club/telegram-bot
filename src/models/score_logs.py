from pydantic import BaseModel, Field
from datetime import datetime


class ScoreLog(BaseModel):
    id: str | None = None
    user_telegram_id: str
    timestamp: datetime
    points: int = Field(..., gt=0)
    reason: str
