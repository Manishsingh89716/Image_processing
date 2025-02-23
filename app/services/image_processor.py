from PIL import Image
import requests
from io import BytesIO

# function for compressing the image if required
def compress_image(image_url: str) -> str:
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        output = BytesIO()
        image.save(output, format=image.format, quality=50)
        return f"compressed_{image_url}"  # Simulate output URL
    return ""