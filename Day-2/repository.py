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