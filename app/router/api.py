from fastapi import APIRouter
from router import food,tip


router = APIRouter()

router.include_router(food.router, prefix="/test", tags=["api/test 예시"])
router.include_router(tip.router, prefix="/bigquery", tags=["api/bigquery 예시"])








