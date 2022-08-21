from question_model import Question
from data import question_data

question_bank = []                      #Criando um banco de perguntas com objetos 
for question in question_data:
    question_text = question_data["text"]
    question_answer = question_data["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

print(question_bank)

