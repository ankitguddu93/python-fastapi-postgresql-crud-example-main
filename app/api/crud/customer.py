from app.api.models.customer import CustomerSchema
from app.db import customer, database
from sqlalchemy import func

async def post(payload: CustomerSchema):
    print("payload   ",payload)
    query = (
        customer
        .insert()
        .values(
            first_name=payload.first_name,
            last_name=payload.first_name,
            mobile=payload.mobile,
            created_date=func.now()
        )
        .returning(customer.c.id)
    )
    print("query   ",query)
    inserted_id = await database.execute(query)
    print("inserted_id   ",inserted_id)
    return inserted_id

async def get(id: int):
    query = customer.select().where(id == customer.c.id)
    return await database.fetch_one(query)
    

async def get_all():
    query = customer.select()
    return await database.fetch_all(query)


async def put(id:int, payload=CustomerSchema):
    query = (
        customer.update().where(id == customer.c.id).values(first_name=payload.first_name, last_name=payload.last_name, mobile=payload.mobile)
        .returning(customer.c.id)
    )
    return await database.execute(query)

async def delete(id:int):
    query = customer.delete().where(id == customer.c.id)
    return await database.execute(query)
    