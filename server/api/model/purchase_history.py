from datetime import datetime
from datetime import timezone

from api.model.order import OrderModelOut
from pydantic import BaseModel
from pydantic import Field

class PurchaseHistoryModel(BaseModel):
    client_id: str
    date: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    orders: list[OrderModelOut]
    total_price: float

class PurchaseHistoryModelOut(PurchaseHistoryModel):
    id: str

    def model_dump(self, *args, **kwargs):
        original_dict = super().model_dump(*args, **kwargs)
        return {'id': self.id, **original_dict}
