from app.services.lead_service import LeadService

class LeadController:

    @staticmethod
    def create_lead(data):
        return LeadService.create_lead(data)

    @staticmethod
    def list_leads():
        return LeadService.get_all_leads()

    @staticmethod
    def qualify_lead(lead_id: int):
        return LeadService.qualify_lead(lead_id)
