from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



-----


https://replit.com/@appbrewery/quiz-game-final?v=1#main.py

class User:
  def __init__(self, user_id, username):
    print("new user being created...")
    self.id=user_id
    self.username=username
  
user_1 = User("001", "alex")
def follow (self, user):
  user.followers ++ 1
  self.following += 1

#user_1.id = "001"
#user_1.username = "alex"

#print(user_1.username)

#constructor - initializing an object


#def function():
  #pass
