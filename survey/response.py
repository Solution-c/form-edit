from typing import Dict, List

from bson.objectid import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from pymongo import ReturnDocument

from database import client
from survey.schemas import Response


db = client.survey
collection = db["rspns"]
router = APIRouter(prefix="/rspns", tags=[""])

@router.post("/", status_code=201, response_model=Response)
async def create(request: Response) -> dict:
    new_article = await collection.insert_one(jsonable_encoder(request))
 
    document = await collection.find_one_and_update(
        {"_id": new_article.inserted_id}, {"$set":{"id": str(new_article.inserted_id)}}
    , return_document=ReturnDocument.AFTER)
    return document