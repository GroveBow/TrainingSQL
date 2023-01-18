import sqlalchemy
from .db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'owners'
    owner_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    owner_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    owner_surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    owner_phone = sqlalchemy.Column(sqlalchemy.String, nullable=False)


