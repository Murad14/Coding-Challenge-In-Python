from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.quiz_icon = PhotoImage(file="images/icon.png")
        self.window.iconphoto(False, self.quiz_icon)
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg= THEME_COLOR)
        self.score_label.grid(row= 0, column=1)

        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0,columnspan=2, pady=50)

        t_button = PhotoImage(file="images/true.png")
        self.t_button = Button(image=t_button, highlightthickness=0, borderwidth=0, command= self.true_pressed)
        self.t_button.grid(row=2, column=0)

        f_button = PhotoImage(file="images/false.png")
        self.f_button = Button(image=f_button, highlightthickness=0, borderwidth=0, command= self.false_pressed)
        self.f_button.grid(row=2, column=1)

        # reset_button = PhotoImage(file="images/reset.png")
        # self.reset_button = Button (image=reset_button, highlightthickness=0, borderwidth=0,command= self.reset_pressed)
        # self.reset_button.grid(row=0, column=0, padx=46, pady=10)

        self.get_next_question()

        self.window.mainloop()

    # def for_reset(self) -> list:
    #     question_bank = []
    #     question_data = QuizBrain(q_list=QuizInterface).next_question()
    #     for question in question_data:
    #         question = question["question"], question["correct_answer"]
    #         question_bank.append(question)
    #     return question_bank
    #
    # def reset_pressed(self):
    #     self.question_bank = self.for_reset()
    #     self.quiz_brain = QuizBrain(self.question_bank)
    #     self.get_next_question()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You've reached the end of the quiz")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


