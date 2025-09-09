#Ручки для ответов
from fastapi import APIRouter, status, HTTPException
from question.schemas import QuestionBase,QuestionResponse
from question.models import QuestionDB
from answer.schemas import AnswerCreate,AnswerResponse
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
            raise HTTPException(status_code=404, detail="Вопрос не найден")
        
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
        raise HTTPException(status_code=500, detail=f"Ошибка: {str(e)}")
    
@answer_router.get("/answers/{id}", response_model=AnswerResponse, status_code=status.HTTP_200_OK)
async def get_answer(id: int, session: SessionDep):
    try:
     
        query = select(AnswerDB).where(AnswerDB.id == id)
        result = await session.execute(query)
        answer = result.scalar_one_or_none()
        
        if not answer:
            raise HTTPException(status_code=404, detail="Ответ не найден")
        
        return answer
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка: {str(e)}")
    
@answer_router.delete("/answers/{id}", status_code=status.HTTP_200_OK)
async def delete_answer(id: int, session: SessionDep):
    try:
        # Сначала проверяем существование ответа
        query = select(AnswerDB).where(AnswerDB.id == id)
        result = await session.execute(query)
        answer = result.scalar_one_or_none()
        
        if not answer:
            raise HTTPException(status_code=404, detail="Ответ не найден")
        
        # Удаляем ответ
        await session.delete(answer)
        await session.commit()
        
        return {"message": f"Ответ с id={id} успешно удалён"}
        
    except HTTPException:
        raise
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка: {str(e)}")