# Lista de Compras Inteligente

Aplicação Streamlit para gerenciar compras, registrar histórico e usar autenticação com login do Google.

## Visão geral

O projeto combina uma interface em Streamlit, persistência local em SQLite e integração com IA para processar notas fiscais e auxiliar na organização da lista de compras. A aplicação usa login com Google configurado no Streamlit para liberar o acesso à interface.

## Funcionalidades

- Login com Google via `st.login()` e controle de acesso com `st.user`.
- Cadastro manual de produtos e importação de histórico em CSV.
- Leitura de nota fiscal com apoio de IA.
- Análise de compras com consultas SQL no banco local.

## Estrutura do repositório

- [main.py](main.py) - Entrada principal da aplicação Streamlit.
- [gen_ai.py](gen_ai.py) - Integração com o modelo de IA.
- [init_data.csv](init_data.csv) - Base inicial de exemplo.
- [prompt_template.md](prompt_template.md) - Template de prompt.
- [query_inteligente.sql](query_inteligente.sql) - Consulta principal usada no app.
- [query.sql](query.sql) - Consultas SQL auxiliares.
- [resposta_template.json](resposta_template.json) - Estrutura esperada da resposta da IA.

## Requisitos

- Python 3.10+ recomendado.
- Ambiente virtual recomendado.
- Dependências instaladas com `pip install -r requirements.txt`.
- Para autenticação, o pacote `streamlit[auth]` precisa estar instalado e configurado no Streamlit.

## Configuração da autenticação

O Streamlit usa o arquivo `.streamlit/secrets.toml` para configurar o login com Google. O que você precisa cadastrar no Google Cloud é um cliente OAuth 2.0 com `client_id` e `client_secret`; no app, o Streamlit ainda usa `redirect_uri`, `cookie_secret` e a URL de metadados do Google para completar o fluxo de login.

Para desenvolvimento local, o callback normalmente é `http://localhost:8501/oauth2callback`. Se você rodar em outra porta, ajuste esse valor no secrets e também no Google Cloud.

### Exemplo de secrets

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "troque-por-uma-chave-longa-e-aleatoria"

[auth.google]
client_id = "seu-client-id.apps.googleusercontent.com"
client_secret = "seu-client-secret"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

## Como rodar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run main.py
```

## Observações

- O banco local é [database.db](database.db) e usa SQLite.
- Não comite credenciais reais no repositório.
- Use o arquivo de exemplo de secrets como base para o ambiente local.
