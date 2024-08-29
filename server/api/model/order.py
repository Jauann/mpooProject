class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        item_pedido = ItemPedido(produto, quantidade)
        self.itens.append(item_pedido)

    def obter_total(self):
        return sum(item.produto.preco * item.quantidade for item in self.itens)
