# Doceria — BMVC (Bottle)

Loja de doces com pedido pelo WhatsApp, organizada na estrutura BMVC
(Bottle + Model + View + Controller).

## Trabalhando com o BMVC no BASH:

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python route.py

Acesse: http://localhost:8080 (a porta pode ser trocada com a variável `PORT`).

## Trabalhando com o BMVC no DOCKER:

1. $ docker build -t bmvci .
1. $ docker run -d -p 8080:8080 -v $(pwd):/bmeta bmvci

(ou execute `bmvc_setup.sh`)

## Estrutura

- route.py                          -> rotas (GET /, POST /pedido, GET /healthz); só delegam ao controller
- config.py                         -> número do WhatsApp e nome da loja (variáveis de ambiente)
- app/controllers/application.py    -> classe Application (único controller: `pages` + `render`)
- app/controllers/datarecord.py     -> classe DataRecord (lê o "banco" JSON)
- app/controllers/db/doces.json     -> catálogo de doces
- app/models/                       -> Doce e Pedido (regras e validação)
- app/views/html/                   -> base.tpl, index.tpl, _docinho.tpl (SimpleTemplate do Bottle)
- app/static/                       -> css/style.css, js/app.js

## Variáveis de ambiente

- `WHATSAPP_NUMERO` — número que recebe os pedidos (padrão no `config.py`)
- `LOJA_NOME` — nome exibido no site
- `PORT` — porta do servidor (padrão: 8080)
