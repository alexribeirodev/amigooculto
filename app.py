import streamlit as st
import pandas as pd
from crypto_utils import decrypt_text

st.set_page_config(page_title="Amigo Oculto de Natal")

id = st.query_params.get("id")

if not id:
    st.error("Acesso inválido!")
else:
    try:
        df = pd.read_csv("names.csv")
        row = df[df["unique_code"] == id]
        if not row.empty:
            assigned_name = decrypt_text(row.iloc[0]["to"])
            st.write(f"## Olá, {row.iloc[0]["name"]}!")
            st.write("A pessoa selecionada para você dar o presente é:")
            st.write(f"# {assigned_name}")
        else:
            st.error("ID inválido foi provisionado")
    except Exception as e:
        st.error(f"Um erro aconteceu: {str(e)}")
