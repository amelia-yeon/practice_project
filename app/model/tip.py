from typing import List, Set, Union
from pydantic import BaseModel


class TipRequest(BaseModel):
    gender : Union[str, None] = None


class TipResponse(BaseModel):
    total_bill: Union[int, None] = None
    tip: Union[int, None] = None
    gender: Union[str, None] = None
    smoker: Union[bool, None] = None
    day: Union[str, None] = None
    time: Union[str, None] = None
    size: Union[int, None] = None















