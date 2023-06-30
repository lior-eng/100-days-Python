import html

class QuizBrain:
    
    def __init__(self, q_list: list,
                 q_number: int = 0,
                 score: int = 0) -> None:
        self.question_list = q_list        
        self.question_number = q_number
        self.score = score
        self.current_question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)
    
    def next_question(self) -> None:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
    
    def check_answer(self, user_answer: str) -> bool:
        correct_answer: str = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
    
    def final_score(self, score: int, list_length: int) -> None:
        print("You've completed the Quiz")
        print(f"Your score is: {score} / {list_length}")