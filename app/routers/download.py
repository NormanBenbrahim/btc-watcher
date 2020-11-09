from fastapi import APIRouter
from datetime import datetime
from typing import List
from pytz import timezone
from dateutil.relativedelta import relativedelta
import requests
from google.cloud import firestore
from viewmodels.download import PriceInput, PriceOutput, Item

# initialize the router
router = APIRouter()

# initialize the database (cloud datastore)
# TODO: create the firestore database below
db = firestore.Client()
collection = db.collection('features')


@router.get("downloaded/?")
async def list() -> List[PriceOutput]:
    """
    docs
    """
    results = List[PriceOutput] = []

    for doc in collection.stream():
        results.append(to_output_model(doc))
    
    return results 


@router.post("/downloaded/?")
async def create(price: PriceInput) -> PriceOutput:
    """
    docs
    """
    doc_ref = collection.document()
    doc_ref.set(get_db_dict(price))

    return to_output_model(doc_ref.get())


@router.get("downloaded/?")
async def list() -> List[PriceOutput]:
    """
    docs
    """
    results: List[PriceOutput] = []
    for doc in collection.stream():
        results.append(to_output_model(doc))
    return results


@router.post("downloaded/?")
async def create(price: PriceInput) -> PriceOutput:
    """
    docs
    """
    doc_ref = collection.document()
    doc_ref.set(get_db_dict(price))
    return to_output_model(doc_ref.get())


@router.get("downloaded/{download_id}/?")
async def retrieve(download_id: str) -> PriceOutput:
    """
    docs
    """
    doc_ref = collection.document(download_id)
    return to_output_model(doc_ref.get())


@router.put("/downloaded/{download_id}/?")
async def replace(download_id: str, price: PriceInput):
    """
    docs
    """
    doc_ref = collection.document(download_id)
    doc_ref.set(get_db_dict(price))
    return to_output_model(doc_ref.get())


def get_db_dict(price: PriceInput) -> dict:
    """
    docs
    """
    data = price.dict()
    data["start"] = data["start"].isoformat()
    data["end"] = data["end"].isoformat()
    return data


def to_output_model(document) -> PriceOutput:
    """
    docs
    """
    return PriceOutput(id=document.id, **document.to_dict())