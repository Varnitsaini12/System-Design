from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class ShortenRequest(BaseModel):
    long_url: HttpUrl

class ShortenResponse(BaseModel):
    short_url: str
    short_code: str

class UrlOut(BaseModel):
    id: int
    short_code: Optional[str]
    long_url: str
    created_at: datetime
    click_count: int

    class Config:
        orm_mode = True