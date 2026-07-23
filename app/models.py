from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from config.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    category = Column(String)

    supplier = Column(String)

    buy_price = Column(Float)

    sell_price = Column(Float)

    quantity = Column(Integer)

    description = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.now
    )