from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
 
class BaseController:
    def __init__(self, prefix: str, tags: list, resource_name: str, service_class):
        self.router = APIRouter(prefix=prefix, tags=tags)
        self.resource_name = resource_name
        self.service_class = service_class
        self.add_crud_routes()

    def add_crud_routes(self):
        @self.router.get("/")
        async def get_all(db: AsyncSession = Depends(get_db)):
            service = self.service_class(db)
            return await service.get_all()

        @self.router.get("/{item_id}")
        async def get_by_id(item_id: int, db: AsyncSession = Depends(get_db)):
            service = self.service_class(db)
            item = await service.get_by_id(item_id)
            if not item:
                raise HTTPException(status_code=404, detail=f"{self.resource_name.capitalize()} not found")
            return item

        @self.router.post("/")
        async def create_item(data: dict, db: AsyncSession = Depends(get_db)):
            service = self.service_class(db)
            return await service.create(data)

        @self.router.put("/{item_id}")
        async def update_item(item_id: int, data: dict, db: AsyncSession = Depends(get_db)):
            service = self.service_class(db)
            updated = await service.update(item_id, data)
            if not updated:
                raise HTTPException(status_code=404, detail=f"{self.resource_name.capitalize()} not found")
            return updated

        @self.router.delete("/{item_id}")
        async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
            service = self.service_class(db)
            success = await service.delete(item_id)
            if not success:
                raise HTTPException(status_code=404, detail=f"{self.resource_name.capitalize()} not found")
            return {"message": f"{self.resource_name.capitalize()} deleted"}
