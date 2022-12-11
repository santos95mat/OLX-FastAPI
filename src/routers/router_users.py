from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session

from src.schema import schemas
from src.infra.sqlachemy.repositories.user import UserRepository
from src.infra.sqlachemy.config.database import get_db

router = APIRouter()

@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOutput)
def createUser(user: schemas.User, db: Session = Depends(get_db)):
    data = UserRepository(db).create(user)
    return data