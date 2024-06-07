import os
from fastapi.routing import APIRoute
import base64
from pathlib import Path
from core.config import app_config 
# from io import BytesIO
import uuid
from PIL import Image
import imghdr

# Constants for validation
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
ALLOWED_FILE_TYPES = {"jpeg", "png", "gif"}

def generate_uuid_filename():
    return uuid.uuid4()

def process_image_data(image_data: str, file_name: str, folder_name: str) -> [str, str]:
    # if file_name is None or image_data is None:
    #     return None, "image data not provided right!"
    try:
        # Decode the base64 string
        image_bytes = base64.b64decode(image_data)

        # Check the file size
        if len(image_bytes) > MAX_FILE_SIZE:
            return None, "File size exceeds the maximum limit of 5 MB"

        # Check the file type
        file_type = imghdr.what(None, h=image_bytes)
        if file_type not in ALLOWED_FILE_TYPES:
            return None, f"Invalid file type: {file_type}. Allowed types: {', '.join(ALLOWED_FILE_TYPES)}"

        # Save the decoded image data to a file
        upload_dir = app_config.get('images_path')
        os.makedirs(upload_dir, exist_ok=True)
        new_filename = generate_uuid_filename()
        file_path = Path(upload_dir + f"/{new_filename}.{file_type}")
        with file_path.open("wb") as buffer:
            buffer.write(image_bytes)

        return Path(str(file_path)).name, None
        
        
        # file_path = "upload/image.png"
        # # Ensure the upload directory exists
        # os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # # Write the binary data to a file
        # with open(file_path, "wb") as file:
        #     file.write(image_bytes)
        # print(file_path)
        # print(file_path)
        # print(file_path)
        # return file_path, None

    except base64.binascii.Error:
        return None, "Invalid base64 string"
    except Exception as e:
        return None, str(e)