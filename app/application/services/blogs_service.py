# app/application/services/blogs_service.py

from app.application.services.base_service import BaseService
from app.infrastructure.repositories.blogs_repository import BlogRepository
from sqlalchemy.ext.asyncio import AsyncSession

class BlogService(BaseService):
    def __init__(self, session: AsyncSession):
        super().__init__(BlogRepository, session)
