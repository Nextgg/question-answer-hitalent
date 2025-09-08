import uvicorn
from fastapi import FastAPI
from database import engine, Base
from question.models import QuestionDB
from answer.models import AnswerDB
from question.router import question_router
from answer.router import answer_router

app = FastAPI()

app.include_router(question_router)
app.include_router(answer_router)

@app.post ('/setup_database')
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok":True}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)