from typing import Dict, List

from bson.objectid import ObjectId
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from database import client
from survey.schemas import Survey

db = client.survey
collection = db["survey"]
router = APIRouter(prefix="/survey", tags=[""])

@router.post("/", status_code=201, response_model=Survey)
async def create(request:Survey) -> dict:
    new_article = await collection.insert_one(jsonable_encoder(request))
    created_article = await collection.find_one(
        {"_id": new_article.inserted_id}
    )

    created_article["id"] = str(created_article["_id"])

    return created_article