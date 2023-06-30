from tkinter import *
from quiz_brain import QuizBrain
from datetime import time
THEME_COLOR = "#375362"

class QuizInterface():
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)
        
        self.score_label = Label(text= "Score: 0/0", bg= THEME_COLOR,
                                 fg= "white")
        self.score_label.grid(row= 0, column= 1)
        
        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.question_text = self.canvas.create_text(150, 125,
                                    width= 280,
                                    text="Question text",
                                    fill= THEME_COLOR,
                                    font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan= 2, pady= 50)
        
        V_picture = PhotoImage(file="./Day-34/images/true.png")
        self.true_button = Button(image= V_picture,
                                  highlightthickness= 0,
                                  command= self.check_true_answer)
        self.true_button.grid(row= 2, column= 0)
        
        X_picture = PhotoImage(file="./Day-34/images/false.png")
        self.false_button = Button(image= X_picture,
                                   highlightthickness= 0,
                                   command= self.check_false_answer)
        self.false_button.grid(row= 2, column= 1)

        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self) -> None:
        self.canvas.config(bg= "white")
        if self.quiz.still_has_questions():
            self.score_label.config(text= f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "Well done, no more questions")
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")      
              
    def check_true_answer(self) -> None:
        is_right: bool = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_false_answer(self) -> None:
        is_right: bool = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(1000, self.get_next_question)            