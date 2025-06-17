from fastapi import APIRouter
from pydantic import BaseModel
from app.logic import handle_translation_input

router = APIRouter()

class TranslationRequest(BaseModel):
    input: str
    direction: str  # "Latin to Decimal" or "Decimal to Latin"

@router.get("/")
def root():
    return {"message": "Welcome to Latin Numerals API"}

@router.post("/translate")
def translate(req: TranslationRequest):
    result = handle_translation_input(req.input, req.direction)
    return {"result": result}