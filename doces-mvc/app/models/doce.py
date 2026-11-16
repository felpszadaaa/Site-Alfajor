from dataclasses import dataclass


@dataclass(frozen=True)
class Doce:
    id: str
    nome: str
    preco: float
    categoria: str
    cor: str
    topo: str
    


class DoceRepositorio:
    """Fonte dos dados da vitrine. Para usar um banco depois, só este arquivo muda."""

    _DOCES = (
        Doce("alfajor", "Brigadeiro tradicional", 6.00, "brigadeiros", "#e8c48c", "#2b1410"),
        Doce("alfajor", "Brigadeiro de ninho", 6.00, "brigadeiros", "#e8c48c", "#e4ded0"),
        Doce("alfajor", "Beijinho", 6.00, "tradicionais", "#e8c48c", "#d9d2c0"),
        Doce("alfajor", "Nutella", 7.00, "tradicionais", "#e8c48c", "#674e3c"),
        Doce("alfajor", "Paçoca", 7.00, "tradicionais", "#e8c48c", "#e4be65"),
        Doce("alfajor", "Brigadeiro de maracujá", 6.00, "finos", "#e8c48c", "#fe802c"),
        Doce("alfajor", "Alfajor de doce de leite", 6.00, "tradicionais", "#e8c48c", "#a8602a"),
    )

    def todos(self):
        return list(self._DOCES)

    def buscar(self, doce_id):
        for d in self._DOCES:
            if d.id == doce_id:
                return d
        return None

    def por_ids(self, ids):
        return [d for d in (self.buscar(i) for i in ids) if d]
