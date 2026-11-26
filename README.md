<<<<<<< HEAD
# Doceria — Flask em arquitetura BMVC (sem Docker)
=======
# Ju Alfajor Doceria — Flask em arquitetura MVC (sem Docker)
>>>>>>> ab4f443be31c34d7c0d3789bb340f8da2101831a

## Rodar
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
<<<<<<< HEAD
    python route.py
Acesse: http://localhost:5000

## Estrutura (BMVC)
- route.py                       -> rotas (GET /, POST /pedido) que só delegam ao controller
- app/controllers/application.py -> classe Application (único controller)
- app/models/                    -> Doce, DoceRepositorio, Pedido (regras e validação)
- app/views/html/                -> base.html, index.html, _docinho.html (Jinja)
- app/static/                    -> css/style.css, js/app.js
=======
    python run.py
Acesse: http://localhost:5000

## Estrutura (BMVC)
- Model:      app/models/      -> Doce, DoceRepositorio, Pedido (regras e validação)
- View:       app/views/       -> templates Jinja + app/static (CSS, JS)
- Controller: app/controllers/ -> rotas: GET / e POST /pedido

>>>>>>> ab4f443be31c34d7c0d3789bb340f8da2101831a
