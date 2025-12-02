from fastapi import APIRouter
from app.schemas.onboarding import (
    CompanySignupRequest,
    CompanySignupResponse
)
from app.controllers.onboarding_controller import OnboardingController

router = APIRouter(prefix="/auth", tags=["Onboarding"])

@router.post("/company_signup", response_model=CompanySignupResponse)
def signup_company(data: CompanySignupRequest):
    return OnboardingController.signup(data)
