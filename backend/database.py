from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/codeassist")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Schema ---
class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    action_type = Column(String) # 'generation' or 'debugging'
    input_snippet = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"DB Connect Error (Expected during Docker startup build phase): {e}")

def save_log(action: str, content: str):
    db = SessionLocal()
    log = AuditLog(action_type=action, input_snippet=content)
    db.add(log)
    db.commit()
    db.close()

def get_recent_snippets():
    # Mock return for frontend demo if DB isn't populated
    return [
        {"id": 1, "code": "def hello(): pass", "description": "Mock History Item 1"},
        {"id": 2, "code": "print('world')", "description": "Mock History Item 2"}
    ]