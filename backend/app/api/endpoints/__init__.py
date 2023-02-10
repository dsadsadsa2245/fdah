from fastapi import APIRouter

from api.endpoints import user

base_router = APIRouter()

base_router.include_router(user.router)
