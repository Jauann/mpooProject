import os
import uuid

from api.model.product import ProductModel
from api.model.product import ProductOut
from core.config import Config
from core.error import ErrorNotFound
from data.database import Database

class DatabaseProducts:
    PRODUCTS_PATH = str(os.path.join(Config.DATA_FOLDER, Config.PRODUCTS_FILE))

    @staticmethod
    def get() -> list[ProductOut]:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        data_list = [ProductOut(id=key, name=value['name'], price=value['price'], quantity=value['quantity']) for key, value in data["data"].items()]
        return data_list

    @staticmethod
    def get_by_id(id: str) -> ProductOut:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        product = data['data'].get(id)
        if product is None:
            raise ErrorNotFound(message=f'Product "{id}", not found')
        return ProductOut(id=id, name=product['name'], price=product['price'], quantity=product['quantity'])

    @staticmethod
    def create(product: ProductModel | list[ProductModel]) -> ProductOut | list[ProductOut]:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        if isinstance(product, ProductModel):
            id = str(uuid.uuid4())
            data['data'][id] = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
            }
            Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data=data)
            return ProductOut(id=id, name=product.name, price=product.price, quantity=product.quantity)
        products: list[ProductOut] = []
        for p in product:
            id = str(uuid.uuid4())
            data['data'][id] = {
                'name': p.name,
                'price': p.price,
                'quantity': p.quantity,
            }
            products.append(ProductOut(id=id, name=p.name, price=p.price, quantity=p.quantity))
        Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data=data)
        return products

    @staticmethod
    def update(id: str, product: ProductModel) -> ProductOut:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        if id in data['data']:
            data['data'][id] = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
            }
            Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data=data)
            return ProductOut(id=id, name=product.name, price=product.price, quantity=product.quantity)
        raise ErrorNotFound(message=f'Product "{id}", not found')

    @staticmethod
    def delete_by_id(id: str) -> bool:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        if id in data['data']:
            del data['data'][id]
            return Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data=data)
        raise ErrorNotFound(message=f'Product "{id}", not found')

    @staticmethod
    def delete():
        return Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data={'data': {}})
