from fastapi import APIRouter, HTTPException, Request, status
from app.core.security import decode_access_token

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

    try:
        payload = decode_access_token(token)
    except ValueError:
        raise HTTPException(
            detail="Unauthorized",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return {
        "user_id": payload.get("user_id"),
        "name": payload.get("name"),
        "role": payload.get("role"),
    }
    