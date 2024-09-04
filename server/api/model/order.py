from pydantic import BaseModel
from pydantic import Field


class OrderModel(BaseModel):
    product_id: str
    quantity: int = Field(gt=0, description='The quantity must be greater than zero')


class OrderModelOut(OrderModel):
    product_name: str
    product_price: float


# class OrderProduct:
#     def __init__(self, product: ProductModel, quantity: int):
#         self.id = product.id
#         self.price = product.price
#         self.quantity = quantity
#
# class Order:
#     def __init__(self, id_pedido, cliente):
#         self.id_pedido = id_pedido
#         self.cliente = cliente
#         self.itens = []
#
#     def adicionar_item(self, produto, quantidade):
#         item_pedido = ItemPedido(produto, quantidade)
#         self.itens.append(item_pedido)
#
#     def obter_total(self):
#         return sum(item.produto.preco * item.quantidade for item in self.itens)
#
# class Customer:
#     def __init__(self) -> None:
#         self.id: str
#         self.name:str
#         self.orders: list[OrderProduct]
#
