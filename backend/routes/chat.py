from fastapi import APIRouter
from schemas.chat import ChatRequest
from services.llm import ask_llm

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    result = ask_llm(request.query)
    return {"response": result}