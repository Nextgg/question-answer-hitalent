import uvicorn
from fastapi import FastAPI
from database import engine, Base
from question.models import Question
from answer.models import Answer

app = FastAPI()


@app.post ('/setup_database')
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok":True}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)