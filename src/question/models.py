from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)