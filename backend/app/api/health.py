from  fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["API Health Check"],
)

@router.get("/")
async def health_check():
    return {"status": "OK"}