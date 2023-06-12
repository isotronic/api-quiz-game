from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", font=("Arial", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0, pady=20, padx=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.quiz_text = self.canvas.create_text(
            150,
            125,
            text="Quiz Text",
            font=("Arial", 12, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.answer_true)
        self.true_button.grid(column=0, row=2, pady=20, padx=20)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)