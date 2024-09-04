import json
import os
import uuid
from typing import Any

from api.model.product import ProductModel
from api.model.product import ProductOut
from api.model.purchase_history import PurchaseHistory
from core.config import Config

class Database():
    @staticmethod
    def _write(file_path: str, data: dict[Any, Any]) -> bool:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True

    @staticmethod
    def _read(file_path: str) -> dict[Any, Any]:
        data = {}
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

class DatabaseProducts():
    PRODUCTS_PATH: str = os.path.join(Config.PROJECT_FOLDER,  Config.DATA_FOLDER, Config.PRODUCTS_FILE)

    @staticmethod
    def get() -> list[ProductOut]:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        data_list = [ProductOut(id=key, name=value['name'], price=value['price'], quantity=value['quantity']) for key, value in data["data"].items()]
        return data_list

    @staticmethod
    def get_by_id(id: str) -> ProductOut | None:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        product = data['data'][id]
        print(product)
        if not product is None:
            return ProductOut(id=id, name=product['name'], price=product['price'], quantity=product['quantity'])
        return None

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
    def update(id: str, product: ProductModel) -> ProductOut | None:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        if id in data['data']:
            data['data'][id] = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
            }
            Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data=data)
            return ProductOut(id=id, name=product.name, price=product.price, quantity=product.quantity)
        return None

    @staticmethod
    def delete_by_id(id: str) -> bool:
        data = Database._read(file_path=DatabaseProducts.PRODUCTS_PATH)
        if id in data['data']:
            del data['data'][id]
            return Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data=data)
        else:
            return False

    @staticmethod
    def delete():
        return Database._write(file_path=DatabaseProducts.PRODUCTS_PATH, data={'data': {}})


class DatabasePurchases():
    PURCHASES_PATH: str = os.path.join(Config.PROJECT_FOLDER, Config.DATA_FOLDER, Config.PURCHASES_FILE)

    @staticmethod
    def get() -> list[PurchaseHistory]:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        return []

    @staticmethod
    def get_by_id(id: str) -> PurchaseHistory | None:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        return None

    @staticmethod
    def create(history: PurchaseHistory | list[PurchaseHistory]) -> PurchaseHistory | list[PurchaseHistory]:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        return []

    @staticmethod
    def update(id: str, history: PurchaseHistory) -> PurchaseHistory | None:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        return None

    @staticmethod
    def delete_by_id(id: str) -> bool:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        return False

    @staticmethod
    def delete():
        return Database._write(file_path=DatabasePurchases.PURCHASES_PATH, data={'data': {}})

