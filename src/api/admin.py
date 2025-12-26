from src.database.connection import get_database
from src.database.init_db import init_indexes
from fastapi import APIRouter, Header, HTTPException, status
from src.core.config import settings

router = APIRouter(prefix="/api/admin", tags="admin")

router.get("/init-db", response_model=dict, status_code=status.HTTP_200_OK)


async def initialize_db(x_admin_secret: str = Header(...)):
    if x_admin_secret is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="ADMIN_SECRET not configured",
        )
    elif x_admin_secret != settings.admin_secret:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    db = get_database()

    indexes = init_indexes(db)

    return {
        "success": True,
        "message": "Database indexes initialized successfully",
        "indexes_created": indexes,
    }
