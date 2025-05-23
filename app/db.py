import os

from sqlalchemy import (Column, DateTime, Integer, String, Table,Text, create_engine, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/fastapi"
# SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()
blogs = Table(
    "blogs",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255)),
    Column("description", Text),
    Column("created_date", DateTime),
)
customer = Table(
    "customer",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(255)),
    Column("last_name", Text),
    Column("mobile", Integer),
    Column("created_date", DateTime),
)

# Databases query builder
database = Database(DATABASE_URL)
metadata.create_all(engine)