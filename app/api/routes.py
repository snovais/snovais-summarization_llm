from fastapi import APIRouter
from app.services.db_service import insert_text, get_texts, insert_summary, get_summaries
from app.services.summarize_model import summarize_text

router = APIRouter()

@router.post("/add_text")
def add_text(text: str):
    text_id = insert_text(text)
    return {"message": "Texto adicionado com sucesso", "text_id": text_id}

@router.post("/summarize_text")
def summarize(text_id: str):
    texts = get_texts()
    text_obj = next((t for t in texts if str(t["_id"]) == text_id), None)
    if not text_obj:
        return {"error": "Texto não encontrado"}
    summary = summarize_text(text_obj["text"])
    insert_summary(text_id, summary)
    return {"text_id": text_id, "summary": summary}

@router.get("/texts")
def list_texts():
    return get_texts()

@router.get("/summaries")
def list_summaries():
    return get_summaries()
