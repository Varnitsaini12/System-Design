# cache.py

import redis
import json

# Connect to Redis running on localhost:6379
cache = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Save data to cache with TTL (optional)
def set_cache(key: str, value, ttl: int = 30):
    """
    Convert Python object -> JSON -> store in Redis.
    ttl = seconds the cached value stays valid.
    """
    cache.set(key, json.dumps(value), ex=ttl)

def get_cache(key: str):
    """
    Read from Redis, convert JSON -> Python object.
    Returns None if key missing.
    """
    raw = cache.get(key)
    return json.loads(raw) if raw else None

def delete_cache(key: str):
    """Remove key from Redis cache."""
    cache.delete(key)
