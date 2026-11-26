# Doceria — Flask em arquitetura MVC (sem Docker)

## Rodar
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    python route.py
Acesse: http://localhost:5000


## Estrutura (BMVC)
- Model:      app/models/      -> Doce, DoceRepositorio, Pedido (regras e validação)
- View:       app/views/index.html (página única) + app/static (CSS, JS, img)
- Controller: app/controllers/ -> rotas: GET / e POST /pedido

## Fotos dos doces
1. Coloque o arquivo (png ou jpg) em `app/static/img/`.
2. Em `app/models/doce.py`, preencha o campo `imagem` do doce, ex.: `imagem="nutella.png"`.
   Também dá para preencher `descricao="..."`.
