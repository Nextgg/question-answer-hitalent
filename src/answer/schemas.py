#Схемы pydantic
from pydantic import BaseModel
from datetime import datetime

class AnswerBase(BaseModel):
    question_id: int
    user_id: int
    text: str

class AnswerCreate(AnswerBase):
    pass

class AnswerResponse(AnswerBase):
    id: int
    created_at: datetime
    
