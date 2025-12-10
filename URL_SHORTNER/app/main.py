from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
import uvicorn
from database import get_db, engine
import models
import schemas
import service
import asyncio
import repository
from cache import init_redis


# Create DB tables if not present
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Day9 URL Shortener")


# On startup connect to redis
@app.on_event("startup")
async def startup_event():
    await init_redis()


# Health endpoint for LB checks
@app.get("/health")
async def health():
    return {"status": "ok"}


# Endpoint to shorten URL. We accept JSON with long_url.
@app.post("/shorten", response_model=schemas.ShortenResponse)
async def shorten(req: schemas.ShortenRequest, db: Session = Depends(get_db)):
# Business logic handles DB + cache
    result = await service.create_short_url(db, req.long_url)
    return schemas.ShortenResponse(short_url=result["short_url"], short_code=result["short_code"])


# Redirect endpoint: fetch long URL and return 307 temporary redirect
from fastapi.responses import RedirectResponse


@app.get("/{short_code}")
async def redirect_short(short_code: str, db: Session = Depends(get_db)):
    long_url, from_cache = await service.resolve_short_code(db, short_code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")


# Ideally increment click count asynchronously (not blocking redirect). For simplicity, do quick DB update.
# In production you'd push to queue and have worker aggregate counts.
    obj = repository.get_by_short_code(db, short_code)
    if obj:
        obj.click_count = obj.click_count + 1
        db.add(obj)
        db.commit()


# Redirect client to original URL
    return RedirectResponse(url=long_url, status_code=307)