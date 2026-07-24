from brain.decision_engine import DecisionEngine


engine = DecisionEngine()


product = {
    "product": "کره شمال",
    "quantity": 500,
    "buy_price": 100000,
    "sell_price": 120000
}


result = engine.analyze_product(product)

print(result)