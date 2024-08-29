from typing import Annotated
from fastapi import APIRouter, Body, status 
from api.model.product import ProductModel
from api.controller.product import ProductController
from core.response import ResponseJSON

router = APIRouter(prefix='/product')

productController = ProductController()

@router.get('/{id}', response_model=ProductModel, status_code=status.HTTP_200_OK)
async def get(id: str):
    product = productController.search_by_id(id)
    if product is None:
        return ResponseJSON.failure(status_code=status.HTTP_404_NOT_FOUND, message='this product cannot be found')
    return ResponseJSON.successfull(status_code=status.HTTP_200_OK, data=product)

@router.post('/', response_model=ProductModel, status_code=status.HTTP_201_CREATED)
async def create(product: Annotated[ProductModel, Body(embed=True)]):
    new_product = productController.create(product)
    return ResponseJSON.successfull(status_code=status.HTTP_201_CREATED, data=new_product)

@router.put('/{id}', response_model=ProductModel, status_code=status.HTTP_200_OK)
async def update(id: str, product: Annotated[ProductModel, Body(embed=True)]):
    updated_product = productController.update(id, product)
    if updated_product is None:
        return ResponseJSON.failure(status_code=status.HTTP_404_NOT_FOUND, message='this product cannot be found') 
    return ResponseJSON.successfull(status_code=status.HTTP_200_OK, data=updated_product) 

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    is_deleted = productController.remove(id)
    if not is_deleted:
        return ResponseJSON.failure(status_code=status.HTTP_404_NOT_FOUND, message='product not found') 
    return None
