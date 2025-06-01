import redis
import json
from typing import Any, Optional

# Connect to Redis (adjust host/port if needed)
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

CACHE_TTL = 3600  # seconds, e.g. 1 hour

def get_cache(key: str) -> Optional[Any]:
    """
    Retrieve JSON-deserialized value from Redis cache by key.
    Returns None if key does not exist.
    """
    try:
        cached = redis_client.get(key)
        if cached is None:
            return None
        return json.loads(cached)
    except Exception as e:
        # Log error if you want, but silently ignore cache errors here
        return None

def set_cache(key: str, value: Any, ttl: int = CACHE_TTL) -> None:
    """
    Serialize and save a value to Redis cache with TTL (seconds).
    """
    try:
        serialized = json.dumps(value)
        redis_client.setex(key, ttl, serialized)
    except Exception as e:
        # Log error if you want, but silently ignore cache errors here
        pass
