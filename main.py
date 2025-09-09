import uvicorn
from fastapi import FastAPI
import os
from database import Base, engine
from question.models import QuestionDB
from answer.models import AnswerDB
from question.router import question_router
from answer.router import answer_router

app = FastAPI()

# подключаем наши роутеры из сущностей
app.include_router(question_router)
app.include_router(answer_router)

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

# @app.post ('/setup_database')
# async def setup_database():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     return {"ok":True}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)