class QuizBrain:
        #init para definir atributos 
    def __init__(self, q_list):                    
        self.question_nunber = 0            #atributo chamado numero da qestão começabdi com 0.
        self.score = 0                      #atributo de pontuação começando com 0.
        self.question_list = q_list         #Lista de questões será o nosso banco de questoes.
                                            #Ex. QuizBrain(question_bank)
    def still_has_question(self):
        return self.question_nunber < len(self.question_list)  #retorna se é True ou False se o numero da questão for menor que a quantidade na lista de questões. simplifica uma função if else.
         


        #adicionado um método com input para perguntar:
    def next_question(self):               
        current_question = self.question_list[self.question_nunber]
        self.question_nunber +=1                  # para aparecer o número da questão maior que 
                                                #0  na primeira e assim por diante.
        user_answer = input(f"Q.{self.question_nunber}):{current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)  #o metodo next question com o metodo check_answer chamando os parametros user_answer(vem do imput) e a resposta que vem da variavel current_question que será uma lista onde possiu uma chave chamada "answer".

        #adiocionado um método(função) para o objeto que vai checar as respostas:
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():   #verifica se são iguais.
            self.score +=1                                  #se verdadeiro acrescenta ponto na pontuação(score).
            print("You got it rigth!")
        else: 
            print("Thats wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_nunber}\n")
   

