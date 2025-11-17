from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserLogin, UserOut, Token
from app.controllers.user_controller import UserController
from app.utils.auth_user import get_current_user
from app.models.user import User

router = APIRouter(prefix="/user", tags=["users"])
controller = UserController()


@router.post("/adduser", response_model=UserOut)
def add_user(user: UserCreate):
    return controller.register_user(
        name=user.name,
        email=user.email,
        password=user.password,
        role=user.role
    )


@router.post("/login", response_model=Token)
def login(credentials: UserLogin):
    return controller.login_user(
        email=credentials.email,
        password=credentials.password
    )

@router.get("/profile", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user