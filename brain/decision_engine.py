class DecisionEngine:


    def analyze_product(self, product):

        profit = (
            product["sell_price"]
            -
            product["buy_price"]
        )

        margin = (
            profit / product["buy_price"]
        ) * 100


        if product["quantity"] < 100:
            decision = "موجودی کم است، پیشنهاد خرید مجدد"

        elif margin < 15:
            decision = "سود پایین است، بررسی قیمت فروش"

        else:
            decision = "وضعیت محصول مناسب است"


        return {
            "product": product["product"],
            "profit_per_unit": profit,
            "profit_margin": round(margin, 2),
            "decision": decision
        }