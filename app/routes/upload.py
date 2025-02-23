from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ImageRequest
from app.utils import generate_request_id, parse_csv
from app.schemas import UploadRequest
from app.workers.tasks import process_images

router = APIRouter()

# upload the csv file
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload")
def upload_file(request: UploadRequest, db: Session = Depends(get_db)):
    request_id = generate_request_id()

    new_request = ImageRequest(
        request_id=request_id,
        status="processing",
        input_csv=request.csv_file
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    process_images.delay(request_id, request.csv_file)

    return {"request_id": request_id}