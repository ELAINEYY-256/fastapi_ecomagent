from app.services.onboarding_service import OnboardingService
from fastapi import HTTPException, status
from app.services.user_service import UserService


class OnboardingController:

    @staticmethod
    def signup(data):
        # check if company exists. this calls getcompany function by email/phone
        company = UserService.get_company_by_email(data.email)
        if company:
            raise HTTPException(
                status_code=400, detail="Company with this email already exists"
            )
        return OnboardingService.signup_company(data)
