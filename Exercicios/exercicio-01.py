
# Crie uma classe de CadastroPessoa
# Crie uma classe de Cliente que herde da classe CadastroPessoa
# a classe CadastroPessoa deve conter um metodo que informa se a pessoa cadastrada é um cliente Vip ou não
#Exemplo de saída:

class CadastroPessoa:
    def __init__(self, cliente_vip):
        self.vip = cliente_vip # <-- Pode ser um valor true ou falso


class Cliente(CadastroPessoa): 

    def cliente(Self):
        if Self.vip == True:
            print("Sou um cliente vip")
        else :
            print("Sou um cliente normal")



Cliente(cliente_vip = False).cliente()
