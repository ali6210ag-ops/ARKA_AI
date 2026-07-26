from fastapi import APIRouter
from pydantic import BaseModel

from config.database import SessionLocal
from app.models import TradeRequest


router = APIRouter()


class TradeRequestCreate(BaseModel):
    trader_name: str
    product_needed: str
    quantity: int
    budget: float



@router.post("/trade-request")
def create_trade_request(data: TradeRequestCreate):

    db = SessionLocal()


    request = TradeRequest(
        trader_name=data.trader_name,
        product_needed=data.product_needed,
        quantity=data.quantity,
        budget=data.budget
    )


    db.add(request)
    db.commit()
    db.refresh(request)


    db.close()


    return {
        "status": "success",
        "message": "درخواست خرید ثبت شد",
        "request_id": request.id
    }