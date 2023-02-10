from fastapi import FastAPI

from api.endpoints import base_router

app = FastAPI()

app.include_router(base_router)
