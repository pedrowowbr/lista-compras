import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lista Inteligente")

st.markdown("# Lista de compras inteligente!")
st.markdown("## Importar Histórico")

open_file = st.file_uploader("Entre com um arquivo histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df)
