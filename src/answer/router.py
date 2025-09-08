from fastapi import APIRouter, status, HTTPException
from question.schemas import Question,QuestionResponse
from question.models import QuestionDB
from sqlalchemy import select
from utils.dependencies import SessionDep
from datetime import datetime

answer_router = APIRouter()

@answer_router.post("/questions/{id}/answers/")
async def add_answer_to_question