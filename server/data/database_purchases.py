import os
import uuid

from api.model.order import OrderModelOut
from api.model.purchase_history import PurchaseHistoryModel
from api.model.purchase_history import PurchaseHistoryModelOut
from core.config import Config
from data.database import Database

class DatabasePurchases:
    PURCHASES_PATH = str(os.path.join(Config.DATA_FOLDER, Config.PURCHASES_FILE))

    @staticmethod
    def get() -> list[PurchaseHistoryModelOut]:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        history = data['data']
        purchases: list[PurchaseHistoryModelOut] = []
        for key, value in history.items():
            orders = [OrderModelOut(
                product_id=order['product_id'], 
                product_name=order['product_name'],
                product_price=order['product_price'],
                quantity=order['quantity'])  for order in value['orders']
            ]
            purchases.append(PurchaseHistoryModelOut(
                id=key, 
                date=value['date'], 
                client_id=value['client_id'], 
                orders=orders, 
                total_price=value['total_price']
            ))
        return purchases

    @staticmethod
    def create(history: PurchaseHistoryModel) -> PurchaseHistoryModelOut:
        data = Database._read(file_path=DatabasePurchases.PURCHASES_PATH)
        id = str(uuid.uuid4())
        data['data'][id] = {
            'client_id': history.client_id,
            'date': history.date.isoformat(),
            'orders': [order.model_dump() for order in history.orders],
            'total_price': history.total_price
        }
        Database._write(file_path=DatabasePurchases.PURCHASES_PATH, data=data)
        return PurchaseHistoryModelOut(id=id, client_id=history.client_id, orders=history.orders, total_price=history.total_price)

    @staticmethod
    def delete():
        return Database._write(file_path=DatabasePurchases.PURCHASES_PATH, data={'data': {}})

