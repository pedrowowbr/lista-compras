import streamlit as st
import pandas as pd
import sqlalchemy

# Própria máquina
engine = sqlalchemy.create_engine("sqlite:///database.db")

with open("query_inteligente.sql") as query_file:
    query = query_file.read()

st.set_page_config(page_title="Lista Inteligente")

st.markdown("# Lista de compras inteligente!")

try:
    col, _ = st.columns(2)
    numero_dias_adiante = col.number_input("Dias sem voltar ao mercado adiante", min_value=1,
                                           max_value=60,
                                           step=1)
    df_stats = pd.read_sql(query, engine)
    df_stats["comprar"] = df_stats["dias_desde_ultima_compra"] + \
        numero_dias_adiante > df_stats["avg_diff_dias_entre_compras"]
    df_compra = df_stats[df_stats["comprar"]]

except Exception as err:
    print(err)
    df_compra = pd.DataFrame()

if df_stats.empty:
    st.warning("Não há dados históricos suficientes. Registre mais compras!")
else:
    st.dataframe(df_compra)

st.markdown("## Importar Histórico")
open_file = st.file_uploader("Entre com um arquivo histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df)

    if st.button("Registrar Dados!"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")
