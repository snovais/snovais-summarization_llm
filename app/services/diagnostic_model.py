# Instale transformers se necessário: pip install transformers
from transformers import WavLMModel, WavLMProcessor

processor = WavLMProcessor.from_pretrained("microsoft/wavlm-base-plus")
model = WavLMModel.from_pretrained("microsoft/wavlm-base-plus")

"""
Prepare os dados de áudio

Organize os arquivos de áudio por usuário/pessoa.
Use torchaudio para carregar os arquivos.
"""

import torchaudio

waveform, sample_rate = torchaudio.load("caminho/para/audio.wav")

# Extraia embeddings de voz



inputs = processor(waveform, sampling_rate=sample_rate, return_tensors="pt")
with torch.no_grad():
    embeddings = model(**inputs).last_hidden_state.mean(dim=1)

"""Compare embeddings para autenticação

Calcule a distância (cosine similarity) entre embeddings de diferentes áudios.
Defina um threshold para autenticação."""

import torch

def cosine_similarity(a, b):
    return torch.nn.functional.cosine_similarity(a, b)

sim = cosine_similarity(embeddings1, embeddings2)

"""Avalie o sistema

Use métricas como EER (Equal Error Rate) ou ROC curves. """
