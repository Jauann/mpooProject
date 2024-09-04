from api.controller.product import ProductController
from api.model.order import OrderModel
from api.model.order import OrderModelOut
from api.router.stock import ProductOut

product_controller = ProductController()


class OrderController:
    def product_exists(self, product_id: str) -> bool:
        return product_controller.search_by_id(product_id) != None

    def check_quantity_on_stock(self, product_stock: ProductOut, order_product: OrderModel) -> bool:
        return product_stock.quantity <= order_product.quantity

    def create(self, product_id: str, quantity: int) -> OrderModelOut | None:
        product_stock = product_controller.search_by_id(product_id)
        if product_stock is None:
            return None
        return OrderModelOut(product_id=product_stock.id, product_name=product_stock.name, product_price=product_stock.price, quantity=quantity)
