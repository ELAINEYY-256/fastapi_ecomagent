from app.services.user_service import UserService
from fastapi import HTTPException, status
from app.models.user import User
from app.models.branch import Branch
from app.models.company import Company
from app.utils.security import create_access_token


class UserController:

    @staticmethod
    def signup_company(data):
        # check if company exists
        company = UserService.get_company_by_name(data.company_name)
        if company:
            raise HTTPException(
                status_code=400, detail="Company with this name already exists"
            )

        # create company
        company = Company(name=data.company_name)
        newCompany = UserService.create_company(company)

        if newCompany:
            # create head branch
            headBranch = Branch(
                name=f"{newCompany.name} Head Office", company_id=newCompany.id
            )
            newHeadBranch = UserService.create_branch(headBranch)
            # create super user
            if newHeadBranch:
                # create user
                user = User(
                    is_superuser=True,
                    first_name=data.first_name,
                    email=data.email,
                    password_hash=data.password,
                    role="superuser",
                    company_id=newCompany.id,
                    branch_id=newHeadBranch.id,
                )
                newUser = UserService.create_user(user)
                if newUser:
                    # create token
                    token = create_access_token(
                        {
                            "sub": newUser.email,
                            "user_id": newUser.id,
                            "company_id": newCompany.id,
                            "role": newUser.role,
                        }
                    )
                    return {
                        "company_id": newCompany.id,
                        "user_id": newUser.id,
                        "email": newUser.email,
                        "role": newUser.role,
                        "token": token,
                    }
        return None

    @staticmethod
    def register_user(
        name: str, email: str, password: str, role: str, is_superuser: bool = False
    ):

        # check if user exists
        user = UserService.get_user_by_email(email)
        if user:
            raise HTTPException(
                status_code=400, detail="User with this email already exists"
            )

        # create user
        user = User(
            is_superuser=is_superuser,
            first_name=name,
            email=email,
            password_hash=password,
            role=role,
        )
        return UserService.create_user(user)

    @staticmethod
    def login_user(email: str, password: str):
        return UserService.login_user(email, password)
