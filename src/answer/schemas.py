from pydantic import BaseModel
from datetime import datetime

class Answer(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str

class AnswerResponse(BaseModel):
    id: int
    question_id: int
    user_id: int
    text: str
    created_at: datetime