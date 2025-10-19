from app.core.config import db_texts, db_summaries

def insert_text(text: str) -> str:
    result = db_texts.texts.insert_one({"text": text})
    return str(result.inserted_id)

def get_texts():
    return list(db_texts.texts.find({}, {"_id": 1, "text": 1}))

def insert_summary(text_id: str, summary: str):
    db_summaries.summaries.insert_one({"text_id": text_id, "summary": summary})

def get_summaries():
    return list(db_summaries.summaries.find({}, {"_id": 0, "text_id": 1, "summary": 1}))
