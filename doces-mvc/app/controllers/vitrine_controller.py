from flask import Blueprint, render_template

from app.models.doce import DoceRepositorio

bp = Blueprint("vitrine", __name__)
repo = DoceRepositorio()


@bp.get("/")
def index():
    doces = repo.todos()
    destaques = repo.por_ids(["alfajor-tradicional", "alfajor-ninho", "alfajor-beijinho", "alfajor-nutella"])
    return render_template("index.html", doces=doces, destaques=destaques)
