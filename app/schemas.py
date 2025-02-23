from pydantic import BaseModel
from typing import List

class UploadRequest(BaseModel):
    csv_file: str  # Assume base64 encoded CSV for simplicity

class StatusResponse(BaseModel):
    request_id: str
    status: str
    output_csv: str | None
