


# 1) Start dependencies with Docker (MySQL + Redis)
# docker-compose up -d


# 2) Create a virtualenv and install dependencies
# python -m venv venv
# source venv/bin/activate # or venv\Scripts\activate on Windows
# pip install -r requirements.txt


# 3) Copy .env or adjust DATABASE_URL/REDIS_URL


# 4) Start the FastAPI app
# uvicorn main:app --reload --host 0.0.0.0 --port 8000


# 5) Shorten a URL
# POST http://localhost:8000/shorten body: {"long_url": "https://example.com"}


# 6) Visit http://localhost:8000/{short_code} to be redirected
