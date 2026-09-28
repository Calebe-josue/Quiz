import customtkinter as ctk


class ResultadoView(ctk.CTkToplevel):
    def __init__(self, master, resultado):
        super().__init__(master)

        self.resultado = resultado

        self.title("Resultado - JENPEX")
        self.geometry("800x650")

        self.protocol(
            "WM_DELETE_WINDOW",
            self.fechar
        )

        self.criar_interface()

    def criar_interface(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Resultado",
            font=("Arial", 30, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            padx=30,
            pady=(30, 10)
        )

        acertos = self.resultado["acertos"]
        total = self.resultado["total"]
        percentual = self.resultado["percentual"]

        resumo = ctk.CTkLabel(
            self,
            text=f"{acertos}/{total} acertos — {percentual:.1f}%",
            font=("Arial", 28, "bold")
        )

        resumo.grid(
            row=1,
            column=0,
            padx=30,
            pady=10
        )

        scroll = ctk.CTkScrollableFrame(
            self
        )

        scroll.grid(
            row=2,
            column=0,
            padx=30,
            pady=20,
            sticky="nsew"
        )

        for questao in self.resultado["questoes"]:

            self.criar_questao(
                scroll,
                questao
            )

        botao = ctk.CTkButton(
            self,
            text="Fechar",
            command=self.fechar
        )

        botao.grid(
            row=3,
            column=0,
            padx=30,
            pady=20
        )

    def criar_questao(
        self,
        parent,
        questao
    ):

        status = (
            "✓ CORRETA"
            if questao["correta"]
            else "✗ INCORRETA",
        )

        frame = ctk.CTkFrame(
            parent
        )

        frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        pergunta = ctk.CTkLabel(
            frame,
            text=(
                f"{questao['id']}. "
                f"{questao['pergunta']}"
            ),
            font=("Arial", 20, "bold"),
            wraplength=650,
            justify="left"
        )

        pergunta.pack(
            anchor="w",
            padx=15,
            pady=(15, 8)
        )

        resultado = ctk.CTkLabel(
            frame,
            text=status,
            font=("Arial", 20, "bold"),
            text_color="#00FF00" if status=='✓ CORRETA' else "#FF0000"
        )

        resultado.pack(
            anchor="w",
            padx=15,
            pady=5
        )

        resposta_usuario = ctk.CTkLabel(
            frame,
            text=(
                f"Sua resposta: "
                f"{questao['resposta_usuario']}"
            ),
            wraplength=650,
            justify="left",
            font=("Arial",26,'bold')
        )

        resposta_usuario.pack(
            anchor="w",
            padx=15,
            pady=3
        )

        resposta_correta = ctk.CTkLabel(
            frame,
            text=(
                f"Resposta correta: "
                f"{questao['resposta_correta']}"
            ),
            wraplength=650,
            justify="left",
            font=("Arial",26,'bold')
        )

        resposta_correta.pack(
            anchor="w",
            padx=15,
            pady=3
        )

        explicacao = ctk.CTkLabel(
            frame,
            text=(
                f"Explicação: "
                f"{questao['explicacao']}"
            ),
            wraplength=650,
            justify="left",
            font=("Arial",26,'bold')
        )

        explicacao.pack(
            anchor="w",
            padx=15,
            pady=(3, 15)
        )

    def fechar(self):
        self.destroy()