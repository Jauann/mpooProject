import os

import uvicorn
from core.config import Config

Config.PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    uvicorn.run(app='app:app', host=Config.HOST, port=Config.PORT, log_level=Config.LOG_LEVEL, reload=Config.RELOAD)

# from services.inventory_service import ServicoEstoque
# from services.checkout_service import ServicoCheckout
# from models.product import Produto
# from models.customer import Cliente
# from models.order import Pedido
#
# def gerar_nota_fiscal(pedido):
#     print("\n--- Nota Fiscal ---")
#     print(f"Cliente: {pedido.cliente.nome}")
#     print("Itens:")
#     for item in pedido.itens:
#         print(f"{item.produto.nome} - Quantidade: {item.quantidade} - Preço: R${item.produto.preco:.2f}")
#     total = pedido.obter_total()
#     print(f"Total: R${total:.2f}")
#     print("-------------------\n")
#
# def menu():
#     servico_estoque = ServicoEstoque()
#     servico_estoque.carregar_dados()
#     servico_checkout = ServicoCheckout(servico_estoque)
#     servico_checkout.carregar_historico()
#
#     while True:
#         print("1. Adicionar produto ao estoque")
#         print("2. Realizar venda")
#         print("3. Exibir histórico de vendas")
#         print("4. Sair")
#
#         opcao = input("Escolha uma opção: ")
#
#         if opcao == "1":
#             id_produto = int(input("ID do produto: "))
#             nome = input("Nome do produto: ")
#             preco = float(input("Preço do produto: "))
#             estoque = int(input("Quantidade em estoque: "))
#             produto = Produto(id_produto, nome, preco, estoque)
#             servico_estoque.adicionar_produto(produto)
#             print(f"Produto {nome} adicionado com sucesso.")
#         elif opcao == "2":
#             id_cliente = int(input("ID do cliente: "))
#             nome_cliente = input("Nome do cliente: ")
#             cliente = Cliente(id_cliente, nome_cliente)
#             pedido = Pedido(1, cliente)
#
#             while True:
#                 id_produto = int(input("ID do produto (0 para finalizar): "))
#                 if id_produto == 0:
#                     break
#                 quantidade = int(input("Quantidade: "))
#                 produto = servico_estoque.obter_produto(id_produto)
#                 if produto:
#                     pedido.adicionar_item(produto, quantidade)
#                 else:
#                     print("Produto não encontrado.")
#
#             servico_checkout.processar_pedido(pedido)
#             gerar_nota_fiscal(pedido)
#         elif opcao == "3":
#             servico_checkout.exibir_historico()
#         elif opcao == "4":
#             print("Saindo...")
#             break
#         else:
#             print("Opção inválida.")
