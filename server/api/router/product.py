from typing import Annotated

from fastapi import APIRouter
from fastapi import Body
from fastapi import status

from api.controller.product import ProductController
from api.model.product import ProductModel
from api.model.product import ProductOut
from core.response import ResponseJSON

router = APIRouter(prefix='/product')

product_controller = ProductController()


@router.get('/{id}', response_model=ProductOut, status_code=status.HTTP_200_OK)
async def get(id: str):
    product = product_controller.search_by_id(id)
    if product is None:
        return ResponseJSON.failure(status_code=status.HTTP_404_NOT_FOUND, message='this product cannot be found')
    return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=product)


@router.post('/', response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create(product: Annotated[ProductModel, Body(embed=True)]):
    new_product = product_controller.create(product)
    return ResponseJSON.successful(status_code=status.HTTP_201_CREATED, data=new_product)


@router.put('/{id}', response_model=ProductOut, status_code=status.HTTP_200_OK)
async def update(id: str, product: Annotated[ProductModel, Body(embed=True)]):
    updated_product = product_controller.update(id, product)
    if updated_product is None:
        return ResponseJSON.failure(status_code=status.HTTP_404_NOT_FOUND, message='this product cannot be found')
    return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=updated_product)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    is_deleted = product_controller.remove(id)
    if not is_deleted:
        return ResponseJSON.failure(status_code=status.HTTP_404_NOT_FOUND, message='product not found')
