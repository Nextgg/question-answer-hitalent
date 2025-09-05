from pydantic import BaseModel

class answer(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str