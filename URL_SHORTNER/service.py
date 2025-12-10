from sqlalchemy.orm import Session
import repository, utils, cache
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import repository, utils, cache
from dotenv import load_dotenv
import os
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


async def create_short_url(db: Session, long_url: str):
    # 1) persist long_url to get an id
    obj = repository.create_url(db, long_url)


    # 2) generate short code from numeric id
    short_code = utils.encode_base62(obj.id)


    # 3) save short code back to DB
    obj = repository.set_short_code(db, obj, short_code)


    # 4) cache mapping for fast reads
    short_url = f"{BASE_URL}/{short_code}"
    # store: {short_code: long_url}
    await cache.cache_set(f"short:{short_code}", {"long_url": long_url}, ex=24*3600)


    return {"short_url": short_url, "short_code": short_code}


async def resolve_short_code(db: Session, short_code: str):
    # 1) check cache
    cached = await cache.cache_get(f"short:{short_code}")
    if cached:
        return cached["long_url"], True


    # 2) fallback to DB
    obj = repository.get_by_short_code(db, short_code)
    if not obj:
        return None, False


    # 3) update cache for future hits
    await cache.cache_set(f"short:{short_code}", {"long_url": obj.long_url}, ex=24*3600)
    return obj.long_url, False