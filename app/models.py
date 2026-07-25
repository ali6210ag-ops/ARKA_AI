from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from config.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    category = Column(String)

    city = Column(String)

    phone = Column(String)

    description = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.now
    )


class Trader(Base):
    __tablename__ = "traders"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    company = Column(String)

    city = Column(String)

    phone = Column(String)

    description = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.now
    )


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


class TradeRequest(Base):
    __tablename__ = "trade_requests"

    id = Column(Integer, primary_key=True, index=True)

    trader_name = Column(String)

    product_needed = Column(String)

    quantity = Column(Integer)

    budget = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.now
    )