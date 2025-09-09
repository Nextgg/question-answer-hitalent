#Модель базы данных
from databaseutils import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class AnswerDB(Base):
    __tablename__ = "answer"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer,ForeignKey("questions.id"))
    user_id = Column(Integer)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
 
    # Добавляем связь с вопросом
    question = relationship("QuestionDB", back_populates="answers")