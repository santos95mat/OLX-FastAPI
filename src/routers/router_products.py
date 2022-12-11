from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.schema import schemas
from src.infra.sqlachemy.repositories.product import ProductRepository
from src.infra.sqlachemy.config.database import get_db

router = APIRouter()

@router.get('/products', response_model=List[schemas.Product])
def getProducts(db: Session = Depends(get_db)):
    data = ProductRepository(db).getAll()
    return data

@router.get('/products/{id}', response_model=schemas.Product)
def getProduct(id: int, db: Session = Depends(get_db)):
    data = ProductRepository(db).getById(id)
    return data

@router.post('/products', status_code=status.HTTP_201_CREATED, response_model=schemas.Product)
def createProduct(product: schemas.Product, db: Session = Depends(get_db)):
    data = ProductRepository(db).create(product)
    return data

@router.put('/products/{id}', response_model=schemas.Product)
def updateProduct( id: int, product: schemas.Product, db: Session = Depends(get_db)):
    data = ProductRepository(db).update(id, product)
    return data

@router.delete('/products/{id}', status_code=status.HTTP_200_OK)
def deleteProduct(id: int, db: Session = Depends(get_db)):
    data = ProductRepository(db).delete(id)
    return data
