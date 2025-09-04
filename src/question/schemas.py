from pydantic import BaseModel
from datetime import datetime

class Question(BaseModel):
    id: int
    text: str
    created_at: datetime