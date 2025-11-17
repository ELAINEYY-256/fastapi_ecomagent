from app.services.agent_service import AgentService

class AgentController:

    @staticmethod
    def create_agent(data):
        return AgentService.create_agent(data)

    @staticmethod
    def update_agent(agent_id, updates):
        return AgentService.update_agent(agent_id, updates)

    @staticmethod
    def get_agents():
        return AgentService.list_agents()

    @staticmethod
    def get_agent(agent_id):
        return AgentService.get_agent(agent_id)

    @staticmethod
    def delete_agent(agent_id):
        return AgentService.delete_agent(agent_id)
