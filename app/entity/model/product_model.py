from sqlalchemy import Column, Integer, String, Text
from app.infrastructure.database import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Text, nullable=False)
    unit = Column(Text, nullable=False)
