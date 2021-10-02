# Crie uma classe que represente uma calculadora
# A classe deve receber os valores a serem calculados pelo metodo inicializador
# Deve conter os 4 calculos básicos
# - Somar
# - Subtrair
# - Dividir
# - Multiplicar

class calculadora:
    def __init__(self,x,y):
        self.um = x
        self.dois = y

    def somar(self):
        print(self.um + self.dois)
           
    def subtrair(self):
        print(self.um - self.dois)

    def multiplicar(self):
        print(self.um * self.dois)

    def dividir(self):
        print(self.um / self.dois)   

somar = calculadora(10,2)
somar.somar()

subtrair = calculadora(10,2) 
subtrair.subtrair()

multiplicar = calculadora(10,2)
multiplicar.multiplicar()

dividir = calculadora(10,2)
dividir.dividir()




