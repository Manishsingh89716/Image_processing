from fastapi import FastAPI
from app.routes import upload, status
from app.database import init_db

app = FastAPI()

init_db()

app.include_router(upload.router, prefix="/api")
app.include_router(status.router, prefix="/api")
from app.workers.tasks import celery

if __name__ == "__main__":
    celery.worker_main(["worker", "--loglevel=info"])