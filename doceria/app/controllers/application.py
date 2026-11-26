from bottle import template

from config import Config
from app.controllers.datarecord import DataRecord
from app.models.pedido import Pedido


class Application():

    def __init__(self):
        self.pages = {
            'index': self.index
        }

        self.__model = DataRecord()

    def render(self, page, parameter=None):
        content = self.pages.get(page, self.index)
        if not parameter:
            return content()
        else:
            return content(parameter)

    # ---------- páginas ----------
    def index(self):
        return template(
            'app/views/html/index',
            loja=Config.LOJA_NOME,
            moeda=Pedido.moeda,
            doces=self.__model.todos(),
            destaques=self.__model.por_ids(
                ["brigadeiro-tradicional", "ninho", "beijinho", "alfajor-doce-de-leite"]
            ),
        )

    # ---------- ações ----------
    def criar_pedido(self, dados):
        pedido = Pedido.de_dados(dados, self.__model)
        erros = pedido.validar()
        if erros:
            return {"erros": erros}, 400
        return {"url": pedido.url_whatsapp(Config.WHATSAPP_NUMERO)}, 200
