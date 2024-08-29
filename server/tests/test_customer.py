import unittest
from modelos.cliente import Cliente

class TesteCliente(unittest.TestCase):
    def teste_criacao_cliente(self):
        cliente = Cliente(1, "João")
        self.assertEqual(cliente.id_cliente, 1)
        self.assertEqual(cliente.nome, "João")

if __name__ == '__main__':
    unittest.main()
