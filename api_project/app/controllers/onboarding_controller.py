from app.services.onboarding_service import OnboardingService

class OnboardingController:

    @staticmethod
    def signup(data):
        #check if company exists. this calls getcompany function by email/phone
        #conditional statement
        return OnboardingService.signup_company(data)
        
