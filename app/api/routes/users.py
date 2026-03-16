from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/users/me", response_model=UserResponse)
def get_current_user_info(current_user: UserResponse = Depends(get_current_user)):
    return current_user
