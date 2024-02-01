from fastapi import FastAPI
from app.routers import tasks
from app.models.tasks import Task
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(tasks.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)