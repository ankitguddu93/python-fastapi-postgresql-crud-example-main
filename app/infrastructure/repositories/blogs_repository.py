# app/infrastructure/repositories/blogs_repository.py

from app.infrastructure.repositories.base_repository import BaseRepository
from app.domain.model.blog_model import Blog
from sqlalchemy.ext.asyncio import AsyncSession

class BlogRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Blog, session)
