from fastapi import FastAPI
from app.services.summarize_model import Summarizer
from app.services.db_service import insert_text, get_texts, insert_summary, get_summaries

app = FastAPI(title="Summarization Texts NoSQL")

summarizer = Summarizer()

@app.get("/")
def root():
    return {"message": "Summarization API is running 🚀"}

@app.post("/generate_summary/{text_id}")
def generate_summary(text_id: str):
    text_doc = texts_collection.find_one({"_id": text_id})
    if not text_doc:
        return {"error": "Texto não encontrado."}

    text = text_doc["content"]
    summary = summarizer.summarize(text)

    summaries_collection.insert_one({
        "text_id": text_id,
        "summary": summary
    })

    return {"text_id": text_id, "summary": summary}
