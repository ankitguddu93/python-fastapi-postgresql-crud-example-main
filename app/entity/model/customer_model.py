from sqlalchemy import Column, Integer, String, Text
from app.infrastructure.database import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(Text, nullable=False)
    mobile = Column(Text, nullable=False)
