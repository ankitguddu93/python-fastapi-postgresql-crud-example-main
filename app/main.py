from fastapi import FastAPI
from app.api.controller.blogs_controller import router as blog_router
from app.api.controller.customer_controller import router as customer_router

app = FastAPI()
app.include_router(blog_router ,prefix="/api", tags=["blogs"])
app.include_router(customer_router ,prefix="/api", tags=["customer"])
