from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ImageRequest
from app.schemas import StatusResponse

router = APIRouter()

# get the status after uploading csv
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/status/{request_id}", response_model=StatusResponse)
def get_status(request_id: str, db: Session = Depends(get_db)):
    record = db.query(ImageRequest).filter_by(request_id=request_id).first()
    if not record:
        return {"message": "Request ID not found"}
    return StatusResponse(
        request_id=record.request_id,
        status=record.status,
        output_csv=record.output_csv
    )