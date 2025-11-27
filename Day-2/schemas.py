from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):
    text: str
    

class Message(BaseModel):
    id: int
    text: str
    created_at: datetime
    
    class Config:
        from_attributes = True