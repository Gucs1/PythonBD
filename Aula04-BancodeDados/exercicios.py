# Crie um metodo que recebe por input o nome idade e sexo
# esse metodo debe printar na tela uma string formadatada
# Exemplo "Meu nome é joao e tenho 47 anos de idade"
class Pessoa:

    def __init__(self):
        self.nome =input('Digite o seu nome: ')
        self.idade = input ('Digite a sua idade: ')
        self.sexo = input('Digite o seu sexo: ')

    def apresentar(self):
        print(f"Meu nome é {self.nome} tenho {self.idade} anos de idade e meu sexo é {self.sexo}")

voce = Pessoa()
voce.apresentar()

#Crie uma classe de produtos que tenha valor e categoria 
#Essa classe devara conter os metodos getter e setter
#os atributos devem ser privados

#crie uma classe de Testes para a classe de produtos acima
#Testando os valores e passando a ela

#crie uma classse de produto e uma classe de categoria
#essa classe de categoria debe ser passada para um metodo 
#de registro de produto da classe produto
#exemplo produto = Produto()
#>>>>>> categoria = Categoria("Limpeza")

# >>>>> produto.registrar_produto("Sabão em pó, 17.50, categoria")
#>>>>>> print(produto.banco_de_dados)
#>>>>>> {nome:"Sabão em pó", preço:17.50, categoria: Categoria}




