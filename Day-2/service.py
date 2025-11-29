# service.py

from sqlalchemy.orm import Session
import schemas, repository
import cache


# ---- CREATE MESSAGE ----
def create_message_service(db: Session, msg: schemas.MessageCreate):
    # Write to DB
    new_msg = repository.create_message(db, msg)

    # Invalidate list cache (new message added)
    cache.delete_cache("messages_all")

    return new_msg


# ---- LIST MESSAGES ----
def list_messages_service(db: Session):
    # 1. Check Redis cache first
    cached = cache.get_cache("messages_all")
    if cached:
        return cached

    # 2. If not cached -> fetch from DB
    result = repository.list_messages(db)

    # Convert ORM objects -> dicts for caching
    result_dict = [
        {"id": m.id, "text": m.text, "created_at": str(m.created_at)}
        for m in result
    ]

    # 3. Store in Redis for fast future reads
    cache.set_cache("messages_all", result_dict)

    return result_dict


def list_messages_paginated_service(db: Session, skip: int = 0, limit: int = 20):
    return repository.list_messages_paginated(db, skip, limit)
