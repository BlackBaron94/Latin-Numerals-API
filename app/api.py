from fastapi import APIRouter
from pydantic import BaseModel
from app.logic import handle_translation_input, randomize, handle_quiz_input

router = APIRouter()

class TranslationRequest(BaseModel):
    user_input : str
    direction: str  # "Latin to Decimal" or "Decimal to Latin"

class CheckQuizAnswerRequest(BaseModel):
    question_number: str
    user_input : str
    quiz_streak: int

@router.get("/")
def root():
    return {"message": "Welcome to Latin Numerals API"}


@router.post("/translate")
def translate(req: TranslationRequest):
    result = handle_translation_input(req.user_input , req.direction)
    return {"result": result}


@router.post("/quiz_query")
def get_number():
    number = randomize()
    return {"number": number}
    
@router.post("/quiz_answer")
def check_quiz_answer(req: CheckQuizAnswerRequest):
    message, quiz_streak = handle_quiz_input(req.question_number, req.user_input , req.quiz_streak)
    return {"result": message, "streak": quiz_streak}