from fastapi import APIRouter, HTTPException
from typing import Union, List, Dict
from common.exception import *

from controller import tip as ctrl_tip

from model import tip

router = APIRouter()


@router.post('/tip', response_model=Dict[str, List[tip.TipResponse]])
def get_sample(request: tip.TipRequest):
    data = ctrl_tip.get_sample(**request.dict())
    
    return {'data':data}














