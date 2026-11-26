from flask import Flask

from config import Config


def create_app():
    app = Flask(__name__, template_folder="views", static_folder="static")
    app.config.from_object(Config)

    from app.controllers.vitrine_controller import bp as vitrine_bp
    from app.controllers.pedido_controller import bp as pedido_bp

    app.register_blueprint(vitrine_bp)
    app.register_blueprint(pedido_bp)

    @app.template_filter("moeda")
    def moeda(valor):
        texto = f"{valor:,.2f}"
        return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")

    @app.get("/healthz")
    def healthz():
        return "ok", 200, {"Content-Type": "text/plain"}

    return app
