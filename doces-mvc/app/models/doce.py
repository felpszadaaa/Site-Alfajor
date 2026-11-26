from dataclasses import dataclass


@dataclass(frozen=True)
class Doce:
    id: str
    nome: str
    preco: float
    categoria: str
    descricao: str = ""
    imagem: str = ""


class DoceRepositorio:
    """Fonte dos dados da vitrine. Para usar um banco depois, só este arquivo muda."""

    _DOCES = (
        Doce("alfajor-tradicional", "Brigadeiro tradicional", 6.00, "brigadeiros", imagem="alfajor-1.png"),
        Doce("alfajor-ninho", "Brigadeiro de ninho", 6.00, "brigadeiros", imagem="alfajor-2.png"),
        Doce("alfajor-beijinho", "Beijinho", 6.00, "tradicionais", imagem="alfajor-3.png"),
        Doce("alfajor-nutella", "Nutella", 7.00, "tradicionais", imagem="alfajor-1.png"),
        Doce("alfajor-pacoca", "Paçoca", 7.00, "tradicionais", imagem="alfajor-2.png"),
        Doce("alfajor-maracuja", "Brigadeiro de maracujá", 6.00, "finos", imagem="alfajor-3.png"),
        Doce("alfajor-doce-de-leite", "Alfajor de doce de leite", 6.00, "tradicionais", imagem="alfajor-1.png"),
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
