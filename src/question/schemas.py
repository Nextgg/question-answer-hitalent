from pydantic import BaseModel
from datetime import datetime
from answer.schemas import AnswerResponse
from typing import List

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    created_at: datetime
    answers: List[AnswerResponse] = []
    
    class Config:
        from_attributes = True  # Для совместимости с SQLAlchemy моделями