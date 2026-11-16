# Doceria — Flask em arquitetura MVC (sem Docker)

## Rodar
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python run.py
Acesse: http://localhost:5000

## Produção
    gunicorn -w 2 -b 0.0.0.0:8000 "app:create_app()"

## Configurar
    export WHATSAPP_NUMERO=5561988887777
    export LOJA_NOME="Minha Doceria"

## Estrutura (BMVC)
- Model:      app/models/      -> Doce, DoceRepositorio, Pedido (regras e validação)
- View:       app/views/       -> templates Jinja + app/static (CSS, JS)
- Controller: app/controllers/ -> rotas: GET / e POST /pedido
