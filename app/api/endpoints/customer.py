from typing import Any, List
from fastapi import APIRouter, HTTPException, Path, FastAPI

from app.api.crud import customer
from app.api.models.customer import CustomerSchema,CustomerDB

router = APIRouter()


@router.post("/", response_model=CustomerDB, status_code=201)
async def create_customer(payload: CustomerSchema):
    note_id = await customer.post(payload)
    response_object = {
        "id": note_id,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "mobile": payload.mobile,
    }
    return response_object
    
@router.get("/{id}/", response_model=CustomerDB)
async def read_customer(id: int = Path(..., gt=0),):
    note = await customer.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=List[CustomerDB])
async def read_all_customers():
    return await customer.get_all()

@router.put("/{id}/", response_model=CustomerDB)
async def update_customer(payload:CustomerSchema,id:int=Path(...,gt=0)): #Ensures the input is greater than 0
    note = await customer.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_id = await customer.put(id, payload)
    response_object = {
        "id": note_id,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "mobile": payload.mobile,
    }
    return response_object

#DELETE route
@router.delete("/{id}/", response_model=CustomerDB)
async def delete_customer(id:int = Path(...,gt=0)):
    note = await customer.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    await customer.delete(id)

    return note
