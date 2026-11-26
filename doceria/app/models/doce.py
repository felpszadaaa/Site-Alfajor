from dataclasses import dataclass


@dataclass(frozen=True)
class Doce:
    id: str
    nome: str
    preco: float
    categoria: str
    cor: str
    topo: str
    descricao: str = ""
    tipo: str = "brigadeiro"  # "brigadeiro" ou "alfajor" (define o desenho)
