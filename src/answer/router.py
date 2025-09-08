from fastapi import APIRouter, status, HTTPException
from question.schemas import QuestionBase,QuestionResponse
from question.models import QuestionDB
from answer.schemas import AnswerCreate
from answer.models import AnswerDB
from sqlalchemy import select
from utils.dependencies import SessionDep
from datetime import datetime

answer_router = APIRouter()

@answer_router.post("/questions/{question_id}/answers/", response_model=AnswerCreate, status_code=status.HTTP_201_CREATED)
async def add_answer_to_question(
    question_id: int,
    data: AnswerCreate,
    session: SessionDep
):
    try:
        # Проверяем существует ли вопрос
        result = await session.execute(select(QuestionDB).where(QuestionDB.id == question_id))
        question = result.scalar_one_or_none()
        
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Проверяем, что question_id из пути совпадает с данными
        if data.question_id != question_id:
            raise HTTPException(status_code=400, detail="Question ID in path doesn't match request body")
        
        # Создаем ответ
        new_answer = AnswerDB(
            question_id=question_id,
            user_id=data.user_id,
            text=data.text,
            created_at=datetime.now()
        )
        
        session.add(new_answer)
        await session.commit()
        await session.refresh(new_answer)
        
        return {
            "id": new_answer.id,
            "question_id": new_answer.question_id,
            "user_id": new_answer.user_id,
            "text": new_answer.text
        }
        
    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating answer: {str(e)}")