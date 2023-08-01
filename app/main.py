# ================ test  ================ #

# from fastapi import FastAPI
# from typing import Union

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"hello root"}

# @app.get("/world")
# def world():
#     return {"hello world"}

# @app.get("/table/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# ================ test  ================ #

import uvicorn
# import pendulum
import uuid
import contextvars
import time

from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from loguru import logger
from common import exception, utils
from router import  api
from common.utils import *

# ==================================| setting |================================== #



def init_listener(_app: FastAPI) -> None:
    """ 핸들러 초기값 설정 """

    @_app.exception_handler(exception.BaseException)
    async def exception_handler(request: Request, exc: exception.BaseException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        ) 



def init_router(_app: FastAPI) -> None:
    """ 라우터 초기값 설정 """
    
    try:
        _app.include_router(api.router, prefix="/api")

    except Exception as e:
        logger.error(e)


def init_middleware(_app: FastAPI) -> None:
    """ 미들웨어 초기값 설정 """

    @_app.middleware("http")
    async def request_middleware(request: Request, call_next):
        try:
            request_id = str(uuid.uuid4())
            request_id_contextvar.set(request_id)
            
            start_time = time.time() # unix time 형태
            start_time2 = now_time_millisecond() # yyyymmdd HH:mm:ss 형태
            
            response = await call_next(request) 
            
            end_time = time.time()
            end_time2 = now_time_millisecond() # yyyymmdd HH:mm:ss 형태
            
            logger.info(f"{request.client.host} | {request.method} | {request.url} | {response.status_code} | {start_time2} | {end_time2} | {end_time - start_time:.3f}")
            return response
        
        except Exception as e:
            logger.error(f"{request.method} {request.url} >> {e}")
            return JSONResponse(
                status_code=500,
                content={"error_code": 500, "message": "Server Error"}
            )
        finally:
            assert request_id_contextvar.get() == request_id 




def create_app() -> FastAPI:
    """ app 변수 생성 및 초기값 설정 """

    _app = FastAPI(
        title="test",
        description="test for mixed food",
        version="1.0.0",
    )

    init_listener(_app=_app)
    init_router(_app=_app)
    init_middleware(_app=_app)


    return _app

# =============================================================================== #
# ===================================| start |=================================== #
# =============================================================================== #

app = create_app()
request_id_contextvar = contextvars.ContextVar("request_id", default=None) 

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)          
 