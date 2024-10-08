from api.model.product import ProductModel
from api.model.product import ProductOut
from data.database_products import DatabaseProducts


class ProductController:
    def search_by_id(self, id: str) -> ProductOut:
        return DatabaseProducts.get_by_id(id=id)

    def create(self, product: ProductModel) -> ProductOut | list[ProductOut]:
        return DatabaseProducts.create(product)

    def update(self, id: str, product: ProductModel) -> ProductOut:
        return DatabaseProducts.update(id=id, product=product)

    def remove(self, id: str) -> bool:
        return DatabaseProducts.delete_by_id(id=id)
