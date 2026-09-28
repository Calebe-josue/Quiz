import customtkinter as ctk
from tkinter import messagebox

from service.quiz_service import QuizService
from view.resultado_view import ResultadoView


class QuizView(ctk.CTkFrame):
    def __init__(
        self,
        master,
        quiz_service: QuizService
    ):
        super().__init__(master)

        self.quiz_service = quiz_service

        self.resposta_selecionada = ctk.StringVar(
            value=""
        )

        self.criar_interface()
        self.exibir_pergunta()

    def criar_interface(self):
        self.grid_columnconfigure(0, weight=1)
        self.titulo = ctk.CTkLabel(
            self,
            text="QUIZ",
            font=("Arial", 35, "bold")
        )

        self.titulo.grid(
            row=0,
            column=0,
            padx=35,
            pady=(35, 15)
        )

        self.numero = ctk.CTkLabel(
            self,
            text="",
            font=("Arial",15)
        )

        self.numero.grid(
            row=1,
            column=0,
            padx=30,
            pady=10
        )

        self.pergunta_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 20, "bold"),
            wraplength=700,
            anchor='w'
        )

        self.pergunta_label.grid(
            row=2,
            column=0,
            padx=30,
            pady=30,
            sticky='ew'
        )

        self.opcoes_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.opcoes_frame.grid(
            row=3,
            column=0,
            padx=30,
            pady=10,
            sticky="ew"
        )

        self.opcoes_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.botao_proximo = ctk.CTkButton(
            self,
            text="Próxima",
            command=self.processar_resposta,
        )

        self.botao_proximo.grid(
            row=4,
            column=0,
            
            padx=0,
            pady=30,
    
        )

    def exibir_pergunta(self):
        pergunta = self.quiz_service.pergunta_atual
        numero_atual = (self.quiz_service.indice_atual + 1)

        total = len(self.quiz_service.perguntas)

        self.numero.configure(
            text=f"Pergunta {numero_atual} de {total}"
        )

        self.pergunta_label.configure(
            text=pergunta.pergunta
        )

        self.resposta_selecionada.set("")

        for widget in self.opcoes_frame.winfo_children():
            widget.destroy()

        for opcao in pergunta.opcoes:
            radio = ctk.CTkRadioButton(
                self.opcoes_frame,
                text=opcao,
                variable=self.resposta_selecionada,
                value=opcao,
                font=("Arial",26,'bold'),
            )

            radio.pack(
                anchor="w",
                padx=20,
                pady=8
            )

        if self.quiz_service.finalizado:
            self.botao_proximo.configure(
                text="Finalizar"
            )
        else:
            self.botao_proximo.configure(
                text="Próxima"
            )

    def processar_resposta(self):

        resposta = self.resposta_selecionada.get()

        if not resposta:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma resposta antes de continuar."
            )
            return

        self.quiz_service.registrar_resposta(
            resposta
        )

        if self.quiz_service.finalizado:
            self.finalizar_quiz()
        else:
            self.quiz_service.proxima_pergunta()
            self.exibir_pergunta()

    def finalizar_quiz(self):

        resultado = (
            self.quiz_service.calcular_resultado()
        )

        ResultadoView(
            self.master,
            resultado
        )