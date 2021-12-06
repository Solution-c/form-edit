import os
import shutil

from fastapi import File, UploadFile, APIRouter


router = APIRouter(prefix="/upload", tags=[""])

if not os.path.exists("upload"):
    os.mkdir("upload")


@router.post("/")
def save_file(file: UploadFile = File(...)) -> None:
    filepath = f"upload/{file.filename}"
    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()
