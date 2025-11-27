from app.services.branch_service import BranchService

class BranchController:

    @staticmethod
    def create_branch(data):
        return BranchService.create_branch(data)

    @staticmethod
    def list_branches():
        return BranchService.list_branches()

    @staticmethod
    def get_branch(branch_id):
        return BranchService.get_branch(branch_id)

    @staticmethod
    def update_branch(branch_id, updates):
        return BranchService.update_branch(branch_id, updates)

    @staticmethod
    def delete_branch(branch_id):
        return BranchService.delete_branch(branch_id)
