from flask import Blueprint, current_app, jsonify, request

from app.models.doce import DoceRepositorio
from app.models.pedido import Pedido

bp = Blueprint("pedido", __name__)
repo = DoceRepositorio()


@bp.post("/pedido")
def criar_pedido():
    pedido = Pedido.de_dados(request.get_json(silent=True), repo)
    erros = pedido.validar()
    if erros:
        return jsonify({"erros": erros}), 400
    url = pedido.url_whatsapp(current_app.config["WHATSAPP_NUMERO"])
    return jsonify({"url": url})
