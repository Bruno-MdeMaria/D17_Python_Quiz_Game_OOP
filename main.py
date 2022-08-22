from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

question_bank = []                      #Criando um banco de perguntas com objetos 
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


print(question_bank[0].answer)

while quiz.still_has_question():
      quiz.next_question()

print("You finished the quiz.")
print(f"Your final score he was: {quiz.score}/{quiz.question_nunber}")

