class QuizBrain:
    def __init__(self, q_list: list, q_number: int = 0, score: int = 0) -> None:
        self.question_list = q_list        
        self.qustion_number = q_number
        self.score = score

    def still_has_question(self) -> bool:
        return self.qustion_number < len(self.question_list)
    
    def next_question(self) -> None:
        current_question = self.question_list[self.qustion_number]
        self.qustion_number += 1
        user_answer = input(f"Q.{self.qustion_number}: {current_question.text}. (True/False)?: ")
        print(current_question.answer)
        self.check_answer(user_answer, current_question.answer)
        print("\n")
    
    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it right!\n")
            self.score += 1
        else:
            print("Wrong answer")
        print(f"The current answer was {correct_answer}")
        print(f"Your current score {self.score}/{self.qustion_number}")
    
    def final_score(self, score: int, list_length: int) -> None:
        print("You've completed the Quiz")
        print(f"Your score is: {score} / {list_length}")