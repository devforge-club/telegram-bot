import pymongo
from pymongo.asynchronous.database import AsyncDatabase


async def init_indexes(db: AsyncDatabase):
    # Users
    await db.users.create_index("telegram_id", unique=True)
    await db.users.create_index([("record.score", pymongo.DESCENDING)])

    # Score Logs
    await db.score_logs.create_index(
        [("user_telegram_id", pymongo.ASCENDING), ("timestamp", pymongo.DESCENDING)]
    )

    # Tasks
    await db.tasks.create_index("assigned_to")
    await db.tasks.create_index("status")
    await db.tasks.create_index("due_date")

    # Reminders
    await db.reminders.create_index("remind_at")

    # Resources (Text Search)
    await db.resources.create_index([("title", pymongo.TEXT)])
    await db.resources.create_index("category")

    # Events
    await db.events.create_index("date")
