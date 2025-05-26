# app/application/services/customer_service.py

from app.application.services.base_service import BaseService
from app.infrastructure.repositories.customer_repository import CustomerRepository
from sqlalchemy.ext.asyncio import AsyncSession

class CustomerService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomerRepository, session)
