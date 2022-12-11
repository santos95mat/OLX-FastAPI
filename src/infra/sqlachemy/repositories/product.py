from sqlalchemy.orm import Session

from src.schema import schemas
from src.infra.sqlachemy.models import models

class ProductRepository():

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, product: schemas.Product):
        data = models.Product(name=product.name,
                              detail=product.detail,
                              price=product.price,
                              avaible=product.avaible,
                              user_id=product.user_id)
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data

    def getAll(self):
        data = self.db.query(models.Product).all()
        return data

    def getById(self, id: int):
        try:
            data = self.db.query(models.Product).get(id)
        except Exception:
            pass
        finally:
            if data != None:
                return data

    def update(self, id: int, product: schemas.Product):
        data = self.getById(id)
        if data != None:
            self.db.query(models.Product).\
                filter(models.Product.id == id).\
                    update({
                        models.Product.name: product.name,
                        models.Product.detail: product.detail,
                        models.Product.price: product.price,
                        models.Product.avaible: product.avaible
                    })
            self.db.commit()
            self.db.refresh(data)
            return data

    def delete(self, id: int):
        data = self.getById(id)
        if data != None:
            self.db.delete(data)
            self.db.commit()