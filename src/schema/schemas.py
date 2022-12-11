from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    user: str
    password: str

    class Config:
        orm_mode = True

class UserOutput(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    user: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    detail: str
    price: float
    avaible: bool
    
    user_id: int
    user: Optional[User]

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: Optional[int] = None
    quantity: int
    delivery: bool
    comments: str

    class Config:
        orm_mode = True