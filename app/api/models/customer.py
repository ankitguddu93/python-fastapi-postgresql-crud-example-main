from pydantic import BaseModel, Field

class CustomerSchema(BaseModel):
   
    first_name: str = Field(..., min_length=3, max_length=50) #additional validation for the inputs 
    last_name: str = Field(...,min_length=3, max_length=50)
    mobile: str


class CustomerDB(CustomerSchema):
    id: int = Field(primary_key=True, index=True, autoincrement=True)
    first_name: str 
    last_name: str
    mobile: str