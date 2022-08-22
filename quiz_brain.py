class QuizBrain:
        #init para definir atributos 
    def __init__(self, q_list):                    
        self.question_nunber = 0
        self.question_list = q_list         #Lista de questões será o nosso banco de questoes.
                                            #Ex. QuizBrain(question_bank)
    def still_has_question(self):
        return self.question_nunber < len(self.question_list)  #retorna se é True ou False se o numero da questão for menor que a quantidade na lista de questões. simplifica uma função if else.
         


        #adicionado um método com input para perguntar:
    def next_question(self):               
        current_question = self.question_list[self.question_nunber]
        self.question_nunber +=1                  # para aparecer o número da questão maior que 
                                                  #0  na primeira e assim por diante.
        input(f"Q.{self.question_nunber}):{self.current_question.text} (True/False): ") 




