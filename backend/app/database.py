# backend/app/database.py

# 1️⃣ Import needed parts from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 2️⃣ Define our database URL (we’re using SQLite for now)
SQLALCHEMY_DATABASE_URL = "sqlite:///./medprep.db"

# 3️⃣ Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 4️⃣ Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5️⃣ Base class for our ORM models
Base = declarative_base()
