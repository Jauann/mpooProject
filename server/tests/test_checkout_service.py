import unittest
from modelos.produto import Produto
from modelos.cliente import Cliente
from modelos.pedido import Pedido
from servicos.servico_estoque import ServicoEstoque
from servicos.servico_checkout import ServicoCheckout

class TesteServicoCheckout(unittest.TestCase):
    def teste_processar_pedido(self):
        servico_estoque = ServicoEstoque()
        servico_checkout = ServicoCheckout(servico_estoque)

        produto = Produto(1, "Maçã", 0.50, 10)
        servico_estoque.adicionar_produto(produto)

        cliente = Cliente(1, "João")
        pedido = Pedido(1, cliente)
        pedido.adicionar_item(produto, 3)

        servico_checkout.processar_pedido(pedido)
        self.assertEqual(produto.estoque, 7)

if __name__ == '__main__':
    unittest.main()
