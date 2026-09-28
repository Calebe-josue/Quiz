import customtkinter as ctk

from service.json_service import JsonService
from service.quiz_service import QuizService
from view.quiz_view import QuizView


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("JENPEX")
        self.geometry("1280x720")
        self.minsize(700, 600)

        perguntas = JsonService.carregar_perguntas("JENPEX/data/perguntas.json")

        quiz_service = QuizService(perguntas)

        quiz_view = QuizView(self, quiz_service)

        quiz_view.pack(fill="both", expand=True)



app = App()
app.mainloop()