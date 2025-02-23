Image Processing API

Overview

This FastAPI-based application processes images from a CSV file asynchronously. It compresses images, stores them in MySQL, and provides APIs to check processing status.

Features

Upload CSV with image URLs.

Asynchronous image processing using Celery and Redis.

MySQL database integration.

Status API to track processing progress.

Tech Stack

Backend: FastAPI, SQLAlchemy

Database: MySQL

Queue: Celery with Redis

Storage: Local storage for processed images

Installation

pip install -r requirements.txt

Setup

Start MySQL and Redis.

Update .env with database and Redis details.

Initialize the database:

python -c "from app.database import init_db; init_db()"

Run FastAPI server:

uvicorn app.main:app --reload

Start Celery worker:

celery -A app.workers.tasks worker --loglevel=info

API Endpoints

POST /api/upload → Upload CSV

GET /api/status/{request_id} → Check processing status

Testing

Use Postman or CURL to test API endpoints.

License

MIT License
