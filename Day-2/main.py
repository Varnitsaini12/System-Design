from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import schemas, service
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Day 2 Message Service"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""API Endpoints"""

#Default/ root endpoint
@app.get("/", tags=["Root"])
def read_root():
    return {"status": "API is running"}

# Health check endpoint
@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

#Post /messages -> Create new message endpoint
@app.post("/messages", response_model=schemas.Message, tags=["Message"])
def create_message(msg: schemas.MessageCreate, db: Session = Depends(get_db)):
    return service.create_message_service(db, msg)


#Get /messages -> get all the messages
@app.get("/messages", response_model=List[schemas.Message], tags=["Message"])
def get_all_messages(db: Session = Depends(get_db)):
    return service.list_messages_service(db)
