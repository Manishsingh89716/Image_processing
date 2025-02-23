from celery import Celery
from app.database import SessionLocal
from app.models import ImageRequest
from app.utils import parse_csv
from app.services.image_processor import compress_image

# by default celery runs on localhost server
celery = Celery("tasks", broker="redis://localhost:6379/0")


@celery.task()
def process_images(request_id: str, csv_data: str):
    db = SessionLocal()
    record = db.query(ImageRequest).filter_by(request_id=request_id).first()
    if not record:
        return

    parsed_data = parse_csv(csv_data)
    output_data = []

    for row in parsed_data:
        input_urls = row["Input Image Urls"].split(",")
        output_urls = [compress_image(url) for url in input_urls]
        row["Output Image Urls"] = ",".join(output_urls)
        output_data.append(row)

    record.status = "completed"
    record.output_csv = str(output_data)
    db.commit()
    db.close()