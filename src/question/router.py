from fastapi import APIRouter, status, HTTPException
from question.schemas import Question,QuestionResponse
from question.models import QuestionDB
from sqlalchemy import select
from utils.dependencies import SessionDep
from datetime import datetime

question_router = APIRouter()

@question_router.get("/questions", response_model=list[QuestionResponse], status_code=status.HTTP_200_OK)
async def get_questions(session: SessionDep):
    query = select(QuestionDB)
    result = await session.execute(query)
    questions = result.scalars().all()
    return questions

@question_router.post("/questions", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def add_question(data: Question, session: SessionDep):
    try:
        new_question = QuestionDB(
            text= data.text,
            created_at=datetime.now()
        )
        session.add(new_question)
        await session.commit()
        await session.refresh(new_question)  # Обновляем объект чтобы получить ID
        return {"id": new_question.id, "text": new_question.text, "created_at": new_question.created_at}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating question: {str(e)}")
    
@question_router.get("/questions/{id}", status_code=status.HTTP_200_OK)
async def get_questions(session: SessionDep):
    query = select(QuestionDB)
    result = await session.execute(query)
    questions = result.scalars().all()
    return questions