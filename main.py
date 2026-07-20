import streamlit as st
import pandas as pd
import sqlalchemy

# Própria máquina
engine = sqlalchemy.create_engine("sqlite:///database.db")

st.set_page_config(page_title="Lista Inteligente")

st.markdown("# Lista de compras inteligente!")
st.markdown("## Importar Histórico")

open_file = st.file_uploader("Entre com um arquivo histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df)

    if st.button("Registrar Dados!"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")
