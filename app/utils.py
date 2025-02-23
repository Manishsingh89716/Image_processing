import uuid
import csv
import io
from typing import List

def generate_request_id() -> str:
    return str(uuid.uuid4())

def parse_csv(csv_data: str) -> list[str]:
    decoded_data = io.StringIO(csv_data)
    reader = csv.DictReader(decoded_data)
    return [row for row in reader]
