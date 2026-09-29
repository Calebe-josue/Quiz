import json
from pathlib import Path

from models.pergunta import Pergunta


class JsonService:
    
    @staticmethod
    def carregar_perguntas(caminho: str) -> list[Pergunta]:
        caminho_arquivo = Path(caminho)

        if not caminho_arquivo.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        with caminho_arquivo.open("r",encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        perguntas = []

        for item in dados:
            pergunta = Pergunta(
                id=item["id"],
                pergunta=item["pergunta"],
                opcoes=item["opcoes"],
                resposta=item["resposta"],
                explicacao=item["explicacao"]
            )

            perguntas.append(pergunta)

        return perguntas