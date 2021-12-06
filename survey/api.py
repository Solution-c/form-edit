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
async def create(request: Survey) -> dict:
    new_article = await collection.insert_one(jsonable_encoder(request))
    created_article = await collection.find_one({"_id": new_article.inserted_id})
    created_article["id"] = str(created_article["_id"])
    await collection.find_one_and_update(
        {"_id": created_article["_id"]}, {"$set": created_article}
    )
    return created_article


@router.get("/", response_model=Dict[str, List[Survey]])
async def all_surveys(limit: int = 100) -> dict:
    cursor = collection.find()
    documents = []
    for survey in await cursor.to_list(length=limit):
        documents.append(survey)
    return {"all_surveys": documents}


@router.put("/{id}", status_code=202)
async def update(id: str, request: dict):

    survey = await collection.find_one({"_id": ObjectId(id)})

    if survey is None:
        raise HTTPException(
            status_code=404,
            detail=f"No survey is found by provided id: {id}",
        )
    survey["id"] = str(survey["_id"])

    survey = {**survey, **request}
    await collection.find_one_and_update({"_id": survey["_id"]}, {"$set": survey})

    return {"msg": f"A survey of id {id} is updated."}


@router.delete("/{id}")
async def destroy(
    id: str,
):
    delete_result = await collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No survey is found by provided id: {id}",
        )

    return {"msg": f"A survey of id {id} is deleted."}
