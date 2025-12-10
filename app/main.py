from fastapi import FastAPI
from app.api.routers.user_router import router as user_router

app = FastAPI(
    title="Projeto FastAPI - Trabalho de LIP",
    version="0.1.0"
)

app = FastAPI(title="Users LIP API")

app.include_router(user_router)
