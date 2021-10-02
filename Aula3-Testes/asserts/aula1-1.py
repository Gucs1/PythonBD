import unittest

class test(unittest.TestCase):

    # def test_aprendendo_testar(self):
    #     assert 1 == 1

    # def test_strings(self):
    #     assert 1 == "1"
    
    # def test_boleano(self):
    #     assert True == True

    def test_boleano2(self):
        a = "Teste"
        assert bool(a)

    

if __name__ == "__main__":
    unittest.main()