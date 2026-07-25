from gen_ai import generate
import streamlit as st
import pandas as pd
import sqlalchemy
import datetime
import json

import os
import dotenv
dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Própria máquina
engine = sqlalchemy.create_engine("sqlite:///database.db")

with open("query_inteligente.sql") as query_file:
    query = query_file.read()

with open("prompt_template.md") as prompt_file:
    prompt = prompt_file.read()

with open("resposta_template.json") as resposta_file:
    resposta = json.load(resposta_file)


@st.cache_resource(ttl='10min')
def process_nf(prompt, resposta_template, produtos, img_file):
    st.image(open_img)

    prompt_exec = prompt.format(
        produtos="\n".join(produtos), resposta=resposta_template)
    resp = generate(prompt_exec, img_file.getvalue(), img_file.type)
    df = pd.DataFrame(json.loads(resp.text))
    return df


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

st.markdown("## Adicionar Compra")

produtos = df_compra["produto"].unique().tolist()
produtos.sort()
produto = st.selectbox("Produto", options=[
                       "Novo Produto"] + produtos)

if produto == "Novo Produto":
    produto_novo = st.text_input("Inserir novo Produto")
    produto = produto_novo

valor = st.number_input("Valor", min_value=0.01)

if st.button("Registrar Compra"):
    data = {
        "dt_compra": datetime.datetime.now().strftime("%Y-%m-%d"),
        "produto": produto.title(),
        "valor_produto": valor,
    }

    df_insert = pd.DataFrame([data])
    df_insert.to_sql("compras", engine, if_exists="append", index=False)
    st.success("Compra do produto registrada com sucesso!")

st.markdown("## Importar Histórico")
open_file = st.file_uploader("Entre com um arquivo histórico", type="csv")

if open_file:
    df = pd.read_csv(open_file)
    df = st.data_editor(df)

    if st.button("Registrar Dados!"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")

st.markdown("## Importar Nota Fiscal")

open_img = st.file_uploader(
    "Entre com um arquivo de Nota Fiscal", type=["png", "jpeg"])

if open_img:
    df = process_nf(prompt=prompt, resposta_template=resposta,
                    produtos=produtos, img_file=open_img)
    df = st.data_editor(df)
    if st.button("Registrar Dados!"):
        df.to_sql("compras", engine, if_exists="append", index=False)
        st.success("Dados registrados com sucesso!")
