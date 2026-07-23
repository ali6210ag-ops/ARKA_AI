from memory.memory import ARKAMemory
from app.product_service import ProductService


class MarketAgent:

    def __init__(self):
        self.memory = ARKAMemory()
        self.product_service = ProductService()


    def analyze(self, product_name):

        products = self.product_service.get_products()

        found_product = None

        for product in products:
            if product.name == product_name:
                found_product = product
                break


        if found_product:

            result = {
                "product": found_product.name,
                "quantity": found_product.quantity,
                "buy_price": found_product.buy_price,
                "sell_price": found_product.sell_price,
                "status": "Product found and analyzed"
            }

        else:

            result = {
                "product": product_name,
                "status": "Product not found"
            }


        self.memory.save(
            "market_analysis",
            result
        )

        return result



if __name__ == "__main__":

    agent = MarketAgent()

    response = agent.analyze("کره شمال")

    print(response)