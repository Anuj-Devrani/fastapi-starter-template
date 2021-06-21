from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class ItemCreate(ItemBase):
    # Properties to receive on item creation
    title: str


class ItemUpdate(ItemBase):
    # Properties to receive on Item update
    pass


class ItemInDBBase(ItemBase):
    # Properties shared by models stored in DB
    id: int
    title: str

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    # Properties to return to client
    pass


class ItemInDB(ItemInDBBase):
    # Properties properties stored in DB
    pass

