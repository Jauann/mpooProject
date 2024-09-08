from pydantic import BaseModel
from pydantic import Field


class OrderModel(BaseModel):
    product_id: str
    quantity: int = Field(gt=0, description='The quantity must be greater than zero')


class OrderModelOut(OrderModel):
    product_name: str
    product_price: float
