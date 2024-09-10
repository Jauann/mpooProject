from api.controller.purchase_history import PurchaseHistoryController
from core.response import ResponseJSON
from data.database_purchases import PurchaseHistoryModelOut
from fastapi import APIRouter
from fastapi import status

purchase_controller = PurchaseHistoryController()

router = APIRouter(prefix='/history')


@router.get('/', response_model=list[PurchaseHistoryModelOut], status_code=status.HTTP_200_OK)
async def get():
    try:
        data = purchase_controller.get()
        return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=data)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")
