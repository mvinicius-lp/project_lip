from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.user_router import router as user_router
from app.api.routers.study_router import router as study_router
from app.api.routers.discipline_router import router as discipline_router
from app.api.routers.streak_router import router as streak_router
from app.api.routers.dashboard_router import router as dashboard_router
from app.api.routers.report_router import router as report_router

app = FastAPI(
    title="Projeto FastAPI - Trabalho de LIP",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     
    allow_credentials=True,
    allow_methods=["*"],     
    allow_headers=["*"],     
)

app.include_router(user_router)
app.include_router(study_router)
app.include_router(discipline_router)
app.include_router(streak_router)
app.include_router(dashboard_router)
app.include_router(report_router)
