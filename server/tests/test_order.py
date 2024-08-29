import unittest
from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.pedido import Pedido

class TestePedido(unittest.TestCase):
    def teste_total_pedido(self):
        cliente = Cliente(1, "João")
        produto = Produto(1, "Maçã", 0.50, 10)
        pedido = Pedido(1, cliente)
        pedido.adicionar_item(produto, 3)

        self.assertEqual(pedido.obter_total(), 1.50)

if __name__ == '__main__':
    unittest.main()
