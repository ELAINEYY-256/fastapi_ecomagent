from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut, Token
from app.controllers.user_controller import UserController

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
def login(user: UserCreate):
    return controller.login_user(
        email=user.email,
        password=user.password
    )
