from fastapi import APIRouter
from app.schemas.lead import LeadCreate, LeadOut
from app.controllers.lead_controller import LeadController

router = APIRouter(prefix="/leads", tags=["leads"])
controller = LeadController()


@router.post("/", response_model=LeadOut)
def create_lead(lead: LeadCreate):
    return controller.create_lead(lead)


@router.get("/", response_model=list[LeadOut])
def get_all_leads():
    return controller.list_leads()


@router.put("/{lead_id}/qualify", response_model=LeadOut)
def qualify_lead(lead_id: int):
    return controller.qualify_lead(lead_id)
