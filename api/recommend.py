from fastapi import APIRouter

from config.database import SessionLocal
from app.models import TradeRequest
from brain.matching_engine import ARKAMatchingEngine


router = APIRouter()


@router.get("/trade-request/{request_id}/recommend")
def recommend_supplier(request_id: int):

    db = SessionLocal()

    request = (
        db.query(TradeRequest)
        .filter(
            TradeRequest.id == request_id
        )
        .first()
    )

    if request is None:
        db.close()

        return {
            "error": "Request not found"
        }


    engine = ARKAMatchingEngine()

    matches = engine.find_match(
        request.product_needed
    )


    db.close()


    return {
        "request_id": request.id,
        "product": request.product_needed,
        "quantity": request.quantity,
        "budget": request.budget,
        "recommendations": matches
    }