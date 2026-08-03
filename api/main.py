```python
from fastapi import FastAPI
from fastapi.responses import FileResponse

from brain.matching_engine import ARKAMatchingEngine

from config.database import engine, Base
from app.models import Product, Supplier, Trader, TradeRequest

from api.trade_request import router as trade_router
from api.recommend import router as recommend_router


app = FastAPI(
    title="ARKA AI B2B Platform",
    description="AI powered supplier-trader matching system",
    version="0.1"
)


# Create database tables automatically
Base.metadata.create_all(bind=engine)


app.include_router(trade_router)

app.include_router(recommend_router)


@app.get("/")
def home():
    return FileResponse(
        "web/index.html"
    )


@app.get("/match/{product_name}")
def match_supplier(product_name: str):

    matching_engine = ARKAMatchingEngine()

    result = matching_engine.find_match(product_name)

    return {
        "product": product_name,
        "matches": result
    }
```
