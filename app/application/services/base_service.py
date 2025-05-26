# app/application/services/base_service.py

from sqlalchemy.ext.asyncio import AsyncSession

class BaseService:
    def __init__(self, repository_class, session: AsyncSession):
        self.repo = repository_class(session)

    async def get_all(self):
        return await self.repo.get_all()
    
    async def get_by_filter(self, data: dict):
        return await self.repo.get_by_filter(data)
    
    async def get_by_id(self, entity_id: int):
        return await self.repo.get_by_id(entity_id)

    async def create(self, data: dict):
        return await self.repo.create(data)

    async def update(self, entity_id: int, data: dict):
        return await self.repo.update(entity_id, data)

    async def delete(self, entity_id: int):
        return await self.repo.delete(entity_id)
