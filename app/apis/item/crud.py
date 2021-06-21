from typing import List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.apis.item.models import Item


class ItemCRUD:
    model = Item

    def create_item(self, db: Session, item_obj) -> Item:
        item_data = jsonable_encoder(item_obj)
        db_obj = self.model(**item_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_items(self, db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        return db.query(self.model).offset(skip).limit(limit).all()


item = ItemCRUD()
