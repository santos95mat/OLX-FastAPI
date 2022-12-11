from sqlalchemy.orm import Session

from src.schema import schemas
from src.infra.sqlachemy.models import models

class UserRepository():

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, user: schemas.User):
        data = models.User(name=user.name,
                           phone=user.phone,
                           user=user.user,
                           password=user.password)
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data

    def getAll(self):
        data = self.db.query(models.User).scalar().all()
        return data

    def getById(self, id: int):
        try:
            data = self.db.query(models.User).filter_by(id)
        except Exception:
            pass
        finally:
            if data != None:
                return data

    def update(self, id: int, user: schemas.User):
        data = self.getById()
        if data != None:
            self.db.query(models.User).\
                filter(models.User.id == id).\
                    update({
                        models.User.name: user.name,
                        models.User.phone: user.phone,
                        models.User.user: user.user,
                        models.User.password: user.password
                    })
            self.db.commit()
            self.db.refresh(data)
            return data

    def delete(self, id: int):
        data = self.getById(id)
        if data != None:
            self.db.delete(data)
            self.db.commit()