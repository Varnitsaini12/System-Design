from sqlalchemy.orm import Session
import models, schemas

def create_message(db: Session, msg: schemas.MessageCreate):
    new_msg = models.Message(text=msg.text)
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

def list_messages(db: Session):
    return db.query(models.Message).all()

def list_messages_paginated(db: Session, skip: int = 0, limit: int = 20):
    return (
        db.query(models.Message)
        .order_by(models.Message.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def search_messages(db: Session, query: str):
    return db.query(models.Message)\
        .filter(models.Message.text.contains(query))\
        .order_by(models.Message.id.desc())\
        .all()
        
