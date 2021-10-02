  
# Agora que já conhecemos sobre classes e alguns dos seus comportamentos
# Vamos conhecer uma outra pratica muito usada a Herança

# Existem dois tipos de Herança
# - Herança Simples
# - Herança Multipla

# Para este curso abordaremos a Herança simples

# O que é Herança na programação?
#
# Herança como o proprio nome ja diz é herdar algo de sua classe Pai ou SuperClass
# O que uma classe pode herdar para outra pode ser absolutamente tudo

# podemos pensar que a classe Filha e a classe Pai são praticamente a mesma classe pois
# instanciando a classe filha temos as mesmas caracteristicas da classe Pai
# Exemplo:

#class Animal:
    #def __init__(self, patas, calda, som):
       # self.patas = patas
        #self.calda = calda
        #self.som = som

    #def emitir_som(self):
        #print(self.som)

    # Aqui temos a classe Animal que é a classe pai nesse exemplo:
    # Se quisermos uma classe Cachorro por exemplo teriamos que repetir o mesmo código na classe Cachorro
    # Pois um animal pode ter patas, calda e emitir um som


# Como fazemos a Herança?

# Para herdar devemos criar a classe filha e nesta classe ao final do nome abrimos dois parenteses ()
# e passamos para esse parenteses o nome da classe Pai
# Exemplo:

class Animal:
    def __init__(self, patas, calda, som):
        self.patas = patas
        self.calda = calda
        self.som = som

    def emitir_som(self):
        print(self.som)

class Cachorro(Animal):
    
    def nadar(self):
        print("Sou um cachorro e estou nadando")


class Cobra(Animal):
    
    def subir_nas_arvores(self):
        print("So uma cobra e eu subo em arvores")


Cachorro = Cachorro(patas=4, calda=True, som="Au au au")
Cachorro.emitir_som()
Cachorro.nadar()

Cobra = Cobra(patas=0, calda=True, som="ZZZzzzzZZZzzzzZ")
Cobra.emitir_som()
Cobra.subir_nas_arvores

# Percebam que dentro das classes Cachorro e Cobra não existe nenhum comportamento
# Então dessa forma podemos ver que as classes Filhas herdaram de fato o comportamento da classe Pai