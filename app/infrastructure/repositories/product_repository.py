# app/infrastructure/repositories/blogs_repository.py

from app.infrastructure.repositories.base_repository import BaseRepository
from app.entity.model.product_model import Product
from sqlalchemy.ext.asyncio import AsyncSession

class ProductRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Product, session)
