# Lista de Compras - Projeto

Uma aplicação simples para gerenciar listas de compras com suporte a geração/auxílio por IA e consultas SQL.

## Visão geral

Este repositório contém uma pequena aplicação em Python que combina uma interface (provavelmente com Streamlit) e scripts auxiliares para processar dados de itens, gerar respostas usando modelos de linguagem e executar consultas SQL. O objetivo é facilitar a criação e organização de listas de compras, além de permitir experimentos com prompts e consultas automatizadas.

## Estrutura do repositório

- gen_ai.py - Script para integração com modelos de IA (ex.: OpenAI) e geração de texto.
- main.py - Entrada principal da aplicação. Executado com `streamlit run main.py`.
- init_data.csv - Dados iniciais de exemplo (itens, categorias, quantidades, etc.).
- prompt_template.md - Template de prompt usado para chamadas ao modelo de IA.
- query_inteligente.sql - SQL para consultas mais avançadas/inteligentes.
- query.sql - Consultas SQL auxiliares.
- resposta_template.json - Template de resposta JSON para padronizar saídas.

(Arquivos adicionais podem estar presentes; adapte conforme o conteúdo real.)

## Funcionalidades principais

- Gerenciamento básico de itens de compra (adicionar, listar, editar).
- Geração de sugestões ou listas otimizadas via IA (dependendo de `gen_ai.py`).
- Execução de consultas SQL para análise e relatórios.
- Exemplo de integração com templates de prompt e templates de resposta.

## Requisitos

- Python 3.10+ recomendado
- Recomenda-se criar um ambiente virtual

Dependências (veja `requirements.txt` para a lista exata):

```
# Exemplo rápido — recomenda-se usar o arquivo `requirements.txt` abaixo
pip install streamlit pandas SQLAlchemy python-dotenv google-genai
```

## Instalação

1. Clone este repositório:

```
# Lista de Compras Inteligente

Aplicação Streamlit para gerenciar e sugerir compras com suporte a OCR/IA.

## Quick start

Requisitos: Python 3.10+. Use um ambiente virtual.

Instalação rápida:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Configuração mínima: copie `.env.example` para `.env` e defina `GEMINI_API_KEY`.

Executar:

```
streamlit run main.py
```

## Arquivos principais
- `main.py` — app Streamlit
- `gen_ai.py` — integração com Gemini (Google GenAI)
- `init_data.csv`, `prompt_template.md`, `query_inteligente.sql`, `resposta_template.json`

## Dependências
Ver `requirements.txt` (versões travadas). Para gerar novamente após mudanças: `pip freeze > requirements.txt`.

## Observações
- Banco local: `database.db` (SQLite). Não comite chaves em `.env`.
- Para alterações maiores, abra uma issue antes de PR.
