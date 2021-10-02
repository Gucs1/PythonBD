# Crie uma classe de cadastro de produtos
# Essa classe devera herdar da classe categoria
# Devera imprimir na tela para cada Produto com a classe categoria

# Exemplo

class Categoria:
    def __init__(self, Limpeza, Frutas, Doces):
        self.limpeza = Limpeza
        self.frutas = Frutas
        self.doces = Doces

class Produtos(Categoria):
    
    def Bolacha(self):
        print("Sou doce")


Produtos = Produtos(Limpeza=, Frutas=, Doces="sim")
Produtos.Bolacha()
