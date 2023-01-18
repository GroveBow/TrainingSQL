import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'cars'
    car_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    car_color = sqlalchemy.Column(sqlalchemy.String, default="white")
    car_owner = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('owners.owner_id'))
    car_price = sqlalchemy.Column(sqlalchemy.Integer, default='1000')


