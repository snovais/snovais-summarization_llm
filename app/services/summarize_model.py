from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.core.utils import create_prompt

class Summarizer:
    def __init__(self, model_name="google/flan-t5-large"):
        print("🔹 Carregando modelo de sumarização...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        print("✅ Modelo carregado com sucesso!")

    def summarize(self, text: str) -> str:
        prompt = create_prompt(text)
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048)
        outputs = self.model.generate(
            **inputs,
            max_length=800,
            temperature=0.7,
            top_p=0.9
        )
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(type(summary))
        return summary
