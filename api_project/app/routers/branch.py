from fastapi import APIRouter
from app.schemas.branch import BranchCreate, BranchUpdate, BranchOut
from app.controllers.branch_controller import BranchController

router = APIRouter(prefix="/branches", tags=["branches"])

@router.post("/", response_model=BranchOut)
def create_branch(data: BranchCreate):
    return BranchController.create_branch(data)

@router.get("/", response_model=list[BranchOut])
def list_branches():
    return BranchController.list_branches()

@router.get("/{branch_id}", response_model=BranchOut)
def get_branch(branch_id: int):
    return BranchController.get_branch(branch_id)

@router.put("/{branch_id}", response_model=BranchOut)
def update_branch(branch_id: int, data: BranchUpdate):
    return BranchController.update_branch(branch_id, data)

@router.delete("/{branch_id}")
def delete_branch(branch_id: int):
    return BranchController.delete_branch(branch_id)
