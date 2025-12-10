from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class UrlMap(Base):
    __tablename__ = "url_map"
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(16), unique=True, index=True, nullable=True)
    long_url = Column(String(2048), nullable=False)
    created_at = Column(DateTime, default=func.now())
    click_count = Column(Integer, default=0, nullable=False)
