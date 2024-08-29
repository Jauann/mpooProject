import json

class ServicoCheckout:
    def __init__(self, servico_estoque):
        self.servico_estoque = servico_estoque
        self.historico_vendas = []
        self.caminho_historico = "historico_vendas.json"

    def processar_pedido(self, pedido):
        for item in pedido.itens:
            self.servico_estoque.reduzir_estoque(item.produto.id_produto, item.quantidade)
        total = pedido.obter_total()
        self.historico_vendas.append({
            "cliente": pedido.cliente.nome,
            "itens": [
                {"nome": item.produto.nome, "quantidade": item.quantidade, "preco": item.produto.preco}
                for item in pedido.itens
            ],
            "total": total
        })
        self.salvar_historico()
        print(f"Total do pedido: R${total:.2f}")

    def salvar_historico(self):
        with open(self.caminho_historico, 'w') as arquivo:
            json.dump(self.historico_vendas, arquivo, indent=4)
        print("Histórico de vendas salvo com sucesso.")

    def carregar_historico(self):
        try:
            with open(self.caminho_historico, 'r') as arquivo:
                self.historico_vendas = json.load(arquivo)
            print("[✅️] — Histórico de vendas carregado com sucesso.")
        except FileNotFoundError:
            print("Arquivo de histórico de vendas não encontrado. Nenhum dado carregado.")

    def exibir_historico(self):
        print("———————————————————————— [ HISTÓRICO DE VENDAS ] ————————————————————————")
        for venda in self.historico_vendas:
            print(f"Cliente: {venda['cliente']} 👤")
            for item in venda["itens"]:
                print(f" * Produto: {item['nome']} | Quantidade: {item['quantidade']} | Valor: R${item['preco']:.2f}")
            print(f"\nTotal: R${venda['total']:.2f}")
            print("————————")
