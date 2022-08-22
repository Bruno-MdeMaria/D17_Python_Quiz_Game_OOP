class QuizBrain:
    def __init__(self, q_list):             #init para definir atributos         
        self.question_nunber = 0
        self.question_list = q_list         #Lista de questões será o nosso banco de questoes.
                                            #Ex. QuizBrain(question_bank)

    def next_question(self):               #adicionado um método com input para perguntar.
        current_question = self.question_list[self.question_nunber]
        self.question_nunber +=1                  # para aparecer o número da questão maior que 
                                                  #0  na primeira e assim por diante.
        input(f"Q.{self.question_nunber}):{self.current_question.text} (True/False): ") 




