from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlachemy.config.database import Base

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    user = Column(String)
    password = Column(String)

    products = relationship('Product', back_populates='user')

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Float)
    avaible = Column(Boolean)

    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))
    user = relationship('User', back_populates='products')

class Order(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Integer
    delivery = Boolean
    comments = String
