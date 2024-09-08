from typing import Annotated

from api.controller.order import OrderController
from api.controller.order import ProductController
from api.model.order import OrderModel
from core.error import ErrorInvalidInput
from core.error import ErrorNotFound
from core.response import ResponseJSON
from fastapi import APIRouter
from fastapi import Body
from fastapi import status

router = APIRouter(prefix='/order')

order_controller = OrderController()
product_controller = ProductController()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def buy(orders: Annotated[list[OrderModel], Body(embed=True)]):
    try:
        data = order_controller.create(orders=orders)
        return ResponseJSON.successful(status_code=status.HTTP_201_CREATED, data=data)
    except ErrorNotFound as e:
        return ResponseJSON.failure(status_code=e.error_code, message=e.message)
    except ErrorInvalidInput as e:
        return ResponseJSON.failure(status_code=e.error_code, message=e.message)
    except Exception as e:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred")
