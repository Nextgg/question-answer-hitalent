from fastapi import APIRouter, status, HTTPException
from question.schemas import QuestionBase,QuestionResponse,QuestionCreate
from question.models import QuestionDB
from answer.models import AnswerDB
from sqlalchemy import select
from sqlalchemy.orm import selectinload
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
async def add_question(data: QuestionCreate, session: SessionDep):
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
    
@question_router.get("/questions/{id}", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def get_question(id: int, session: SessionDep):
    # Загружаем вопрос вместе с ответами
    query = select(QuestionDB).where(QuestionDB.id == id).options(selectinload(QuestionDB.answers))
    result = await session.execute(query)
    question = result.scalar_one_or_none()
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return question

@question_router.delete("/questions/{id}", status_code=status.HTTP_200_OK)
async def delete_question(id: int, session: SessionDep):
    try:
        # Сначала проверяем существование вопроса
        query = select(QuestionDB).where(QuestionDB.id == id)
        result = await session.execute(query)
        question = result.scalar_one_or_none()
        
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Удаляем вопрос (ответы удалятся автоматически благодаря каскаду)
        await session.delete(question)
        await session.commit()
        
        return {"message": f"Question with id {id} and its answers deleted successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting question: {str(e)}")