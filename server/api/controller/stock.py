from api.model.product import ProductOut
from api.model.product import ProductModel
from data.database import DatabaseProducts


class StockController:
    def get(self) -> list[ProductOut]:
        return DatabaseProducts.get()

    def create(self, products: list[ProductModel]) -> list[ProductOut]:
        new_products = DatabaseProducts.create(products)
        if isinstance(new_products, list):
            return new_products
        return []

    def remove(self):
        return DatabaseProducts.delete()
