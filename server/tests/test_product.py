import unittest
from modelos.produto import Produto

class TesteProduto(unittest.TestCase):
    def teste_reduzir_estoque(self):
        produto = Produto(1, "Maçã", 0.50, 10)
        produto.reduzir_estoque(3)
        self.assertEqual(produto.estoque, 7)

        with self.assertRaises(ValueError):
            produto.reduzir_estoque(8)

if __name__ == '__main__':
    unittest.main()
