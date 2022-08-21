#Classe de usuário como Twiter seguidores:

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.seguidores = 0     #Se quiser colocar na função um valor que precisa iniciar fixo como seguidores... não devemos colocar no parametro da __init__.
        self.seguindo = 0

    def seguir(self, usuario):       #criando um metódo(função) seguir:
        usuario.seguidores += 1                 #variavel usuraio a ser definida(parametro) quando chamar o metodo receberá em seuatibuto "seguidores" +1
        self.seguindo +=1            #o objeto que chamou o metodo receberá em seu atributo "seguindo" +1.

usuario_1 = User("001", "Bruno")
usuario_2 = User("002", "Pricila")

print(usuario_1.username)
print(usuario_1.id)
print(usuario_1.seguidores) 


# usuario 1 passa a seguir usurario 2:

#chamar o metodo para o objeto usuario 1 e colocar no parametro quem está seguindo:
usuario_1.seguir(usuario_2)   

print(usuario_1.seguindo)
print(usuario_1.seguidores)
print(usuario_2.seguidores)
print(usuario_2.seguindo)




