from fastapi import APIRouter, HTTPException, status
from typing import Union, List, Dict
from common.exception import *

from controller import food as ctrl_food

from model import food

router = APIRouter()


@router.get('/{name}')
def get_name(name:str):
    return {'Introduce': f"Hi, my name is {name}"}



@router.post('/define', response_model=Dict[str, food.Define_Item])
def define_item(request:food.Define_Item):
    data = ctrl_food.define_item(**request.dict())
    
    return {'data': data}


# test/food 구현 예시
@router.post('/food', response_model=Dict[str, food.SampleResponse])
def get_test(request: food.SampleRequest):
    data = ctrl_food.get_test(**request.dict())
    
    return {'data':data}


@router.post('/food_v2', response_model=Dict[str, food.SampleResponse])
def get_test(request: food.SampleRequest):
    data = ctrl_food.get_test2(**request.dict())
    
    return {'data': data}

















