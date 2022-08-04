from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.config import get_session, init_db
from .db.model import User, UserCreate, UserRead, UserUpdate

app = FastAPI()

@app.get("/")
async def read_root():
    return {"hello": "world"}

@app.post('/create', response_model=UserRead)
async def create(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User.from_orm(user)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@app.get('/user/{id}', response_model=UserRead)
async def get_user(id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.patch('/user/{id}', response_model=UserRead)
async def update_user(id: int, user: UserUpdate, session: AsyncSession = Depends(get_session)):
    user_db = await session.get(User, id)

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user_db, key, value)
    
    session.add(user_db)
    await session.commit()
    await session.refresh(user_db)
    return user_db

@app.delete('/user/{id}')
async def delete_user(id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await session.delete(user)
    await session.commit()
    return {"ok": True}