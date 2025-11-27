from fastapi import APIRouter
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyOut
from app.controllers.company_controller import CompanyController

router = APIRouter(prefix="/companies", tags=["companies"])

@router.post("/", response_model=CompanyOut)
def create_company(data: CompanyCreate):
    return CompanyController.create_company(data)

@router.get("/", response_model=list[CompanyOut])
def list_companies():
    return CompanyController.list_companies()

@router.get("/{company_id}", response_model=CompanyOut)
def get_company(company_id: int):
    return CompanyController.get_company(company_id)

@router.put("/{company_id}", response_model=CompanyOut)
def update_company(company_id: int, data: CompanyUpdate):
    return CompanyController.update_company(company_id, data)

@router.delete("/{company_id}")
def delete_company(company_id: int):
    return CompanyController.delete_company(company_id)
