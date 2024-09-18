from typing import Annotated

from api.controller.stock import StockController
from api.model.product import ProductModel
from api.model.product import ProductOut
from core.response import ResponseJSON
from fastapi import APIRouter
from fastapi import Body
from fastapi import status

router = APIRouter(prefix='/stock')

stock_controller = StockController()


@router.get('/', response_model=list[ProductOut], status_code=status.HTTP_200_OK)
async def get():
    try:
        data = stock_controller.get()
        return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=data)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")


@router.post('/', response_model=list[ProductOut], status_code=status.HTTP_201_CREATED)
async def create(products: Annotated[list[ProductModel], Body(embed=True)]):
    try:
        data = stock_controller.create(products=products)
        return ResponseJSON.successful(status_code=status.HTTP_201_CREATED, data=data)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete():
    try:
        stock_controller.remove()
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")
