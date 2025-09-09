from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
#Для удобстава использования в ручках

SessionDep = Annotated[AsyncSession, Depends(get_session)]
