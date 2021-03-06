from sqlalchemy import Column, Integer, String

from app.db.session import Base


class Item(Base):

    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(288), index=True,)
    description = Column(String(288), index=True)
