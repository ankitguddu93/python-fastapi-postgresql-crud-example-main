# app/infrastructure/repositories/customer_repository.py

from app.infrastructure.repositories.base_repository import BaseRepository
from app.domain.model.customer_model import Customer
from sqlalchemy.ext.asyncio import AsyncSession

class CustomerRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Customer, session)
