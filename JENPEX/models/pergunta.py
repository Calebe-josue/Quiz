from dataclasses import dataclass
from typing import List


@dataclass
class Pergunta:
    id: int
    pergunta: str
    opcoes: List[str]
    resposta: str
    explicacao: str

    def verificar_resposta(self, resposta_usuario: str) -> bool:
        return resposta_usuario == self.resposta