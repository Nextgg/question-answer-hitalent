from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class Answer(Base):
    __tablename__ = "answer"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(ForeignKey("questions.id"))
    user_id = Column(Integer)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)