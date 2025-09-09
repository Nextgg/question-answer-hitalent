#Модели базы даенных
from databaseutils import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class QuestionDB(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    answers = relationship("AnswerDB", back_populates="question", cascade="all, delete-orphan")