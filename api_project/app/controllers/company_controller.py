from app.services.company_service import CompanyService

class CompanyController:

    @staticmethod
    def create_company(data):
        return CompanyService.create_company(data.name)

    @staticmethod
    def list_companies():
        return CompanyService.list_companies()

    @staticmethod
    def get_company(company_id):
        return CompanyService.get_company(company_id)

    @staticmethod
    def update_company(company_id, data):
        return CompanyService.update_company(company_id, data.name)

    @staticmethod
    def delete_company(company_id):
        return CompanyService.delete_company(company_id)
