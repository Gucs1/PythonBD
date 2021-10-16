import unittest

class test(unittest.TestCase):

    def test_aprendendo_testar(self):
        assert 1 == 1

    def test_strings(self):
        assert 1 == "1"
    
    def test_boleano(self):
        assert True == True

    def test_boleano2(self):
        a = "Teste"
        assert bool(a)

    
    def test_variaveis(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b or a == c
        # or == paava "OU"
        # a é igual a b ou é igual a c?

    def test_valor_inteiro(self):
        assert isinstance(1, int)
    

if __name__ == "__main__":
    unittest.main()