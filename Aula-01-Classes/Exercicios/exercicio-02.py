


class My:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def primeiro(self):
        print('>'*80)

    def ultimo(self):
        print('<'*80)

    def apresentar(self):
        self.primeiro()
        print(f"Olá meu nome é {self.nome} tenho {self.idade} anos e tenho {self.altura} de altura")
        self.ultimo()

Gustavo = My("Gustavo",19,1.81)
Gustavo.apresentar()



