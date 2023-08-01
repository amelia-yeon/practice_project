from typing import List, Set, Union
from pydantic import BaseModel


class Define_Item(BaseModel):
    req_id : Union[str, None] = None
    pw : Union[str, None] = None


class SampleBasicRequest(BaseModel):
    role: Union[str, None] = None
    tools: Union[List[str], None] = None
    mendatory: Union[bool, None] = None


class SampleRequest(BaseModel):
    style: Union[str, None] = None
    grams: Union[List[int], None] = None
    flavor:Union[List[str], None] = None
    tables:Union[List[SampleBasicRequest], None] = None 



# sample response
class SampleBasicRespose(BaseModel):
    num: int 
    style: str 
    role: str 
    tools: str 
    taste: str 
    grams: int 


class SampleResponse(BaseModel):
    count: int 
    dishes: List[dict] 





