from fastapi import APIRouter
from app.schemas.agent import AgentCreate, AgentOut, AgentUpdate
from app.controllers.agent_controller import AgentController

router = APIRouter(prefix="/agents", tags=["agents"])

@router.post("/", response_model=AgentOut)
def create_agent(agent: AgentCreate):
    return AgentController.create_agent(agent)

@router.get("/", response_model=list[AgentOut])
def list_agents():
    return AgentController.get_agents()

@router.get("/{agent_id}", response_model=AgentOut)
def get_agent(agent_id: int):
    return AgentController.get_agent(agent_id)

@router.put("/{agent_id}", response_model=AgentOut)
def update_agent(agent_id: int, updates: AgentUpdate):
    return AgentController.update_agent(agent_id, updates)

@router.delete("/{agent_id}")
def delete_agent(agent_id: int):
    return AgentController.delete_agent(agent_id)
