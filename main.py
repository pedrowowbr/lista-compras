import streamlit as st
import pandas as pd
import sqlalchemy

# Própria máquina
engine = sqlalchemy.create_engine("sqlite:///database.db")

with open("query_inteligente.sql") as query_file:
    query = query_file.read()

try:
    df_stats = pd.read_sql(query, engine)

except Exception as err:
    print(err)
    df_stats = pd.DataFrame()

st.set_page_config(page_title="Lista Inteligente")

st.markdown("# Lista de compras inteligente!")
if df_stats.empty:
    st.warning("Não há dados históricos suficientes. Registre mais compras!")
else:
    st.dataframe(df_stats)

st.markdown("## Importar Histórico")
open_file = st.file_uploader("Entre com um arquivo histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df)

    if st.button("Registrar Dados!"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")
