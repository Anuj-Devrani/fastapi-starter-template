from fastapi import APIRouter

from app.apis.item import api as item_api

api_router = APIRouter()
api_router.include_router(item_api.router, prefix="/items", tags=["items"])