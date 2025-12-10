import os
import json
import asyncio
from dotenv import load_dotenv
load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")


import aioredis


redis = None


async def init_redis():
    global redis
    if redis is None:
        redis = await aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    return redis


async def cache_get(key: str):
    r = await init_redis()
    raw = await r.get(key)
    if not raw:
        return None
    return json.loads(raw)


async def cache_set(key: str, value, ex: int = 3600):
    r = await init_redis()
    await r.set(key, json.dumps(value), ex=ex)


async def cache_del(key: str):
    r = await init_redis()
    await r.delete(key)