from api.controller.purchase_history import PurchaseHistoryController
from data.database_purchases import PurchaseHistoryModelOut
from fastapi import APIRouter
from fastapi import status

purchase_controller = PurchaseHistoryController()

router = APIRouter(prefix='/history')


@router.get('/', response_model=list[PurchaseHistoryModelOut], status_code=status.HTTP_200_OK)
async def get():
    return purchase_controller.get() 
