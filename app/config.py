import os
from dotenv import load_dotenv

load_dotenv()

# connect with mysql database for data retrieval and celery for caching the application
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:12345@localhost/image_processing")
REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")
