from api.model.purchase_history import PurchaseHistoryModel
from api.model.purchase_history import PurchaseHistoryModelOut
from data.database_purchases import DatabasePurchases


class PurchaseHistoryController:
    def get(self) -> list[PurchaseHistoryModelOut]:
        return DatabasePurchases.get()

    def create(self, new_history: PurchaseHistoryModel) -> PurchaseHistoryModelOut:
        return DatabasePurchases.create(new_history)
