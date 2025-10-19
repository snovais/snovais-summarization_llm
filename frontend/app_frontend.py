import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.title("🧠 Text Summary AI")
st.write("Resuma textos automaticamente com o modelo FLAN-T5")

tab1, tab2 = st.tabs(["Adicionar Texto", "Gerar Resumo"])

with tab1:
    new_text = st.text_area("Insira um texto para resumir:")
    if st.button("Salvar texto"):
        response = requests.post(f"{BASE_URL}/add_text", params={"text": new_text})
        if response.status_code == 200:
            st.success("Texto salvo com sucesso!")
            st.json(response.json())
        else:
            st.error("Erro ao salvar o texto")

with tab2:
    st.subheader("Textos disponíveis:")
    texts = requests.get(f"{BASE_URL}/texts").json()

    if len(texts) == 0:
        st.info("Nenhum texto cadastrado ainda.")
    else:
        st.write("Textos recebidos do backend:", texts)  # Mostra os textos para conferência
        # Seleciona o texto diretamente
        selected_text = st.selectbox("Selecione o texto", texts)

        if st.button("Gerar resumo"):
            response = requests.post(
                f"{BASE_URL}/summarize_text",
                params={"text": selected_text}  # envia o texto completo
            )
            if response.status_code == 200:
                st.success("Resumo gerado com sucesso!")
                st.json(response.json())
            else:
                st.error("Erro ao gerar o resumo")


st.divider()
if st.button("Ver todos os resumos"):
    summaries = requests.get(f"{BASE_URL}/summaries").json()
    st.write(summaries)
