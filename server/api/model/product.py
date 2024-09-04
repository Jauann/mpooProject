from pydantic import BaseModel
from pydantic import Field


class ProductModel(BaseModel):
    name: str
    price: float = Field(gt=0, description='The price must be greater than zero')
    quantity: int = Field(gt=0, description='The quantity must be greater than zero')

class ProductOut(ProductModel):
    id: str

# class Produto:
#     def __init__(self, id_produto, nome, preco, estoque):
#         self.id_produto = id_produto
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque
#
#
#     def __str__(self):
#         return f"Produto: {self.nome}{ self.estoque}"
#
#     def reduzir_estoque(self, quantidade):
#         if quantidade > self.estoque:
#             raise ValueError("Quantidade insuficiente em estoque.")
#         self.estoque -= quantidade
