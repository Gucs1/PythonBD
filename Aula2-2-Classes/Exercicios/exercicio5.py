# Crie uma classe de produtos
# que tenha seus atrobutos privados
# Utilizando o getter e o setter para poder alterar seus valores
# sem property

# Crie uma classe de Categorias 
# Que tenha seus atributos privados __
# Utilizando o getter e o setter para poder alterar seus valores 
# Com Property




class Produtos:


    def __init__(self, nome, valor) -> None:
        self.__nome = nome
        self.valor = bebida

    def get_nome(self):
        return self.__nome

    def get_marca(self):
        for bebida in self.__marca:
            print(bebida)

    def set_nome(self, valor):
        self.__nome = valor



produto = Produtos("Coca-Cola", ["Skol", "Pepsi", "Guárana"])
print(produto.get_nome())
produto.set_nome("Fanta")
print(produto.get_nome())
produto.get_marca()


#Exercicio com Property e Setter
class Produtos:

#metodo construtor
    def __init__(self, nome, bebidas) -> None:
        self.__nome = nome
        self.__marca = bebidas

    @property
    def nome(self):
        return self.__nome

    @nome.setter 
    def nome(self, valor):
        self.__nome = valor

    @property
    def marca(self):
        return self.__marca

    @marca.setter 
    def marca(self, skol):
        self.marca = skol


produto = Produtos("Coca-Cola", ["Pepsi", "Guarana", "vodka"])
print(produto.nome)
produto.nome = "Fanta"
print(produto.nome)
print(produto.marca)
produto.marca

