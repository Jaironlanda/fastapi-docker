from typing import Optional
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    name: str
    age: int

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

class UserUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None