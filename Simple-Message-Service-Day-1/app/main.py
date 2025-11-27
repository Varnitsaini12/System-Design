from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from typing import List


app = FastAPI(
    title="Simple Message Service API",
    description="A simple message service to show messages.",
    version="0.1"
)

#messages in memory 

messages_db = []
current_id:int = 1


# Message Models
class MessageCreate(BaseModel):
    msg: str
    
class Message(BaseModel):
    id: int
    msg: str
    created_at: datetime

@app.get("/")
def read_root():
    return {"status": "API is running."}
    

@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.utcnow().isoformat()}

@app.post("/messages", response_model=Message)
def create_message(message: MessageCreate):
    
    """State is stored in memory"""
    global current_id
    
    new_message = Message(
        id=current_id,
        msg=message.msg,
        created_at=datetime.utcnow()   
    )
    
    messages_db.append(new_message)
    current_id +=1
    
    return new_message

@app.get("/messages", response_model=List[Message])
def get_all_messages():
    
    return messages_db