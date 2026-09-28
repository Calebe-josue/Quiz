from models.pergunta import Pergunta


class QuizService:

    def __init__(self, perguntas: list[Pergunta]):
        self.perguntas = perguntas
        self.indice_atual = 0
        self.respostas_usuario = []

    @property
    def pergunta_atual(self) -> Pergunta:
        return self.perguntas[self.indice_atual]

    @property
    def finalizado(self) -> bool:
        return self.indice_atual >= len(self.perguntas) - 1

    def registrar_resposta(self, resposta: str):
        self.respostas_usuario.append(resposta)

    def proxima_pergunta(self):
        if not self.finalizado:
            self.indice_atual += 1

    def calcular_resultado(self) -> dict:

        resultado = []

        acertos = 0

        for pergunta, resposta_usuario in zip(
            self.perguntas,
            self.respostas_usuario
        ):

            correta = pergunta.verificar_resposta(
                resposta_usuario
            )

            if correta:
                acertos += 1

            resultado.append({
                "id": pergunta.id,
                "pergunta": pergunta.pergunta,
                "resposta_usuario": resposta_usuario,
                "resposta_correta": pergunta.resposta,
                "correta": correta,
                "explicacao": pergunta.explicacao
            })

        total = len(self.perguntas)

        percentual = (
            acertos / total * 100
            if total > 0
            else 0
        )

        return {
            "acertos": acertos,
            "total": total,
            "percentual": percentual,
            "questoes": resultado
        }