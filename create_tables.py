# create_tables.py

from sqlalchemy import create_engine
from app.infrastructure.database import Base
from app.entity.model.blog_model import Blog
from app.entity.model.customer_model import Customer
from app.entity.model.product_model import Product

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/fastapi"

def create_tables():
    engine = create_engine(DATABASE_URL)  # ✅ sync engine
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully")

if __name__ == "__main__":
    create_tables()
