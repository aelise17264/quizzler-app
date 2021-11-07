from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = Label(text="Score:", fg="#FFFFFF", bg=THEME_COLOR, pady=20)
        self.score.grid(column=1, row=0, sticky=NE)

        self.scoreboard = Canvas(width=300, height=250)
        self.question_text = self.scoreboard.create_text(
            150,
            125,
            width=280,
            text="First question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.scoreboard.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file="images/true.png")
        self.green = Button(image=true, padx=20, pady=20, highlightthickness=0)
        self.green.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.red = Button(image=false, highlightthickness=0)
        self.red.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # tap into quiz_brain & get next question
        q_text = self.quiz.next_question()
        self.scoreboard.itemconfig(self.question_text, text=q_text)