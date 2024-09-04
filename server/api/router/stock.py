from api.controller.stock import StockController
from api.model.product import ProductModel
from api.model.product import ProductOut
from core.response import ResponseJSON
from fastapi import APIRouter
from fastapi import status

router = APIRouter(prefix='/stock')

stock_controller = StockController()


@router.get('/', response_model=list[ProductOut], status_code=status.HTTP_200_OK)
async def get():
    data = stock_controller.get()
    return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=data)


@router.post('/', response_model=list[ProductOut], status_code=status.HTTP_201_CREATED)
async def create(products: list[ProductModel]):
    data = stock_controller.create(products=products)
    return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=data)


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete():
    stock_controller.remove()
