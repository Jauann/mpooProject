from api.model.order import OrderModel
from pydantic import BaseModel


class PurchaseHistory(BaseModel):
    client_id: str
    products: list[OrderModel]
    total_price: float


class PurchaseHistoryOut(PurchaseHistory):
    id: str
