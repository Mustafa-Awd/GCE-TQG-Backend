from fastapi import APIRouter
from app.services.getTopics import loadTopics
import json


router = APIRouter()



@router.get('/topics:{filename}')
def get_topics(filename: str):
    return loadTopics(filename)