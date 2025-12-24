import os
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.errors import ConfigurationError

_client: AsyncMongoClient | None = None


def get_database() -> AsyncDatabase:
    """
    Returns an AsyncDatabase instance using the Singleton pattern.

    - First call (Cold Start): creates new connection
    - Subsequent calls (Warm Start): reuses existing connection

    Returns:
        AsyncDatabase: MongoDB database instance

    Raises:
        ValueError: If MONGO_URI or DB_NAME are not set
        ConfigurationError: If the MongoDB URI is malformed
        RuntimeError: For unexpected connection errors
    """
    global _client

    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise ValueError("DB_NAME environment variable is required")

    if _client is not None:
        return _client[db_name]

    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise ValueError("MONGO_URI environment variable is required")

    try:
        _client = AsyncMongoClient(
            mongo_uri,
            maxPoolSize=10,
            minPoolSize=1,
            connectTimeoutMS=5000,
            serverSelectionTimeoutMS=5000,
            socketTimeoutMS=10000,
            retryWrites=True,
            retryReads=True,
            compressors="zstd,snappy",
        )
        return _client[db_name]

    except ConfigurationError as e:
        raise ConfigurationError(f"Invalid MongoDB URI format: {str(e)}")

    except Exception as e:
        raise RuntimeError(f"Unexpected error while connecting to MongoDB: {str(e)}")
