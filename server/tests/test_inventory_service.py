import unittest
from modelos.produto import Produto
from servicos.servico_estoque import ServicoEstoque

class TesteServicoEstoque(unittest.TestCase):
    def teste_adicionar_obter_produto(self):
        servico = ServicoEstoque()
        produto = Produto(1, "Maçã", 0.50, 10)
        servico.adicionar_produto(produto)

        self.assertEqual(servico.obter_produto(1), produto)

if __name__ == '__main__':
    unittest.main()
