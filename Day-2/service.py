from sqlalchemy.orm import Session
import schemas, repository

def create_message_service(db: Session, msg: schemas.MessageCreate):
    return repository.create_message(db, msg)

def list_messages_service(db: Session):
    return repository.list_messages(db)