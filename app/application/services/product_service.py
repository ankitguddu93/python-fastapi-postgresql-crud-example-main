# app/application/services/blogs_service.py

from app.application.services.base_service import BaseService
from app.infrastructure.repositories.product_repository import ProductRepository
from sqlalchemy.ext.asyncio import AsyncSession

class ProductService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(ProductRepository, session)
