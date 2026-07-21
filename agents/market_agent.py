from memory.memory import ARKAMemory


class MarketAgent:
    def __init__(self):
        self.memory = ARKAMemory()

    def analyze(self, product_name):
        result = {
            "product": product_name,
            "status": "Market analysis started"
        }

        self.memory.save("market_analysis", result)

        return result


if __name__ == "__main__":
    agent = MarketAgent()

    response = agent.analyze("کره ۱۰۰ گرمی")

    print(response)