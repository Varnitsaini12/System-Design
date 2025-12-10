from sqlalchemy.orm import Session
import models, schemas


def create_url(db: Session, long_url: str):
    obj = models.UrlMap(long_url=long_url)
    db.add(obj)
    db.commit()
    db.refresh(obj) # obj.id is now available
    return obj


def set_short_code(db: Session, obj: models.UrlMap, short_code: str):
    obj.short_code = short_code
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_by_short_code(db: Session, short_code: str):
    return db.query(models.UrlMap).filter(models.UrlMap.short_code == short_code).first()


def get_by_id(db: Session, id: int):
    return db.query(models.UrlMap).filter(models.UrlMap.id == id).first()