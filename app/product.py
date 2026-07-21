from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    id: int
    name: str
    category: str
    supplier_id: int
    buy_price: float
    sell_price: float
    quantity: int
    description: str = ""
    created_at: datetime = datetime.now()