import uuid

from api.controller.product import ProductController
from api.model.order import OrderModel
from api.model.order import OrderModelOut
from api.model.purchase_history import PurchaseHistoryModel
from api.router.purchase_history import PurchaseHistoryController
from api.router.stock import ProductOut
from core.error import ErrorInvalidInput

product_controller = ProductController()
history_controller = PurchaseHistoryController()


class OrderController:
    def has_on_stock(self, product_stock: ProductOut, order: OrderModel) -> bool:
        return product_stock.quantity >= order.quantity

    def calculate_total_price(self, orders: list[OrderModelOut]) -> float:
        return sum(order.product_price * order.quantity for order in orders)

    def create(self, orders: list[OrderModel], client_id: str = str(uuid.uuid4())) -> PurchaseHistoryModel:
        orders_out: list[OrderModelOut] = []
        for order in orders:
            product = product_controller.search_by_id(id=order.product_id)
            if not self.has_on_stock(product, order):
                raise ErrorInvalidInput(message=f'Your demand is for {order.quantity} units of {product.name}, but we only have {product.quantity} in stock')
            product.quantity = product.quantity - order.quantity
            if product.quantity == 0:
                product_controller.remove(id=product.id)
            else:
                product_controller.update(id=product.id, product=product)
            orders_out.append(OrderModelOut(quantity=order.quantity, product_id=product.id, product_name=product.name, product_price=product.price))
        return history_controller.create(new_history=PurchaseHistoryModel(client_id=client_id, orders=orders_out, total_price=self.calculate_total_price(orders_out)))
