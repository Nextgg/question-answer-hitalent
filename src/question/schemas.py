from pydantic import BaseModel
from datetime import datetime

class Question(BaseModel):
    text: str


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime