from fastapi import APIRouter , Request , HTTPException, status , Response

router = APIRouter(
    prefix="/me",
    tags=["Check current status"]
)


@router.get("/")
def get_user(
    request: Request
):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            detail="Unauthorized",
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    
    return Response(
        content={'user' : 'valid'}
    )
    