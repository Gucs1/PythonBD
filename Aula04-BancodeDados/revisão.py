
nome = "bob"

#print(nome)

def dizer_nome(nome):
    print(nome)

dizer_nome(nome)

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

#pessoa = Pessoa(nome, 25)

#print(pessoa.nome, pessoa.idade) OU o metodo abaixo

#print(f"Olá meu nome é {pessoa.nome} e tenho {pessoa.idade} anos de idade \n")
#print("Teste")

#pessoa.Dizer_nome("Eduardt")


class Usuario(Pessoa):
    pass

Usuario("José", 20).dizer_nome("Carlinhos")

