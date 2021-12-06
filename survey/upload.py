import os
import shutil

from fastapi import File, UploadFile, APIRouter


router = APIRouter(prefix="/upload", tags=[""])

if not os.path.exists("uploads"):
    os.mkdir("uploads")


@router.post("/")
def save_file(id: str, qnum: int, file: UploadFile = File(...)) -> None:
    survey_dir_path = f"uploads/{id}"
    file_dir_path = f"{survey_dir_path}/{qnum}"
    if not os.path.exists(survey_dir_path):
        os.mkdir(survey_dir_path)
    if not os.path.exists(file_dir_path):
        os.mkdir(file_dir_path)

    filepath = f"{file_dir_path}/{file.filename}"
    try:
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()
