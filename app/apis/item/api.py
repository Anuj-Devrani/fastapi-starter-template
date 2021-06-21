from typing import Any, List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.apis.item import crud, models, schemas
from app.apis import deps


router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def get_items(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Retrieve items.
    :param db: function to get connection to db
    :param skip: items to skip
    :param limit: no of items to return
    """

    items = crud.item.get_items(db, skip, limit)
    return items


@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.ItemCreate,
) -> Any:
    """
    Create new item.
    """
    item = crud.item.create_item(db=db, item_obj=item_in)
    return item

