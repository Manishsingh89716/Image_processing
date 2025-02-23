from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class ImageRequest(Base):
    __tablename__ = "image_requests"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String(255), unique=True, index=True)  # Add length to VARCHAR
    status = Column(String(50), default="pending")  # Add length to VARCHAR
    input_csv = Column(Text)
    output_csv = Column(Text, nullable=True)
