# app/infrastructure/repositories/base_repository.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class BaseRepository:
    def __init__(self, model, session: AsyncSession):
        self.model = model
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, entity_id: int):
        result = await self.session.execute(select(self.model).where(self.model.id == entity_id))
        return result.scalar_one_or_none()

    async def create(self, data: dict):
        obj = self.model(**data)
        self.session.add(obj)
        await self.session.commit()
