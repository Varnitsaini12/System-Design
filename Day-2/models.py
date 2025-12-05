from sqlalchemy import Column, Integer, String, DateTime, Index
from datetime import datetime
from database import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    
    text = Column(String, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow())

Index("idx_messages_created_at", Message.created_at)
