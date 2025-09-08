from pydantic import BaseModel
from datetime import datetime
from answer.schemas import AnswerResponse
from typing import List

class Question(BaseModel):
    text: str


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime

class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[AnswerResponse] = [] 
    