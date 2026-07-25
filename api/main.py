from fastapi import FastAPI
from fastapi.responses import FileResponse

from brain.matching_engine import ARKAMatchingEngine


app = FastAPI(
    title="ARKA AI B2B Platform",
    description="AI powered supplier-trader matching system",
    version="0.1"
)


@app.get("/")
def home():
    return FileResponse("web/index.html")


@app.get("/match/{product_name}")
def match_supplier(product_name: str):

    engine = ARKAMatchingEngine()

    result = engine.find_match(product_name)

    return {
        "product": product_name,
        "matches": result
    }