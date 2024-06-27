from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB

from database.base import Base


class Accessory(Base):
    __tablename__ = "accessory"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    quantity = Column(Integer)
    images = Column(JSONB)
