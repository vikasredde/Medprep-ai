# backend/app/database.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. load .env file values into environment variables
load_dotenv()

# 2. read DATABASE_URL from environment, if missing use sqlite fallback
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

# 3. create engine differently if sqlite (sqlite needs special connect_args)
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

# 4. session factory - use this to create DB sessions in endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base class for our ORM models
Base = declarative_base()

# 6. Dependency for FastAPI endpoints to get a DB session and close it properly
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

