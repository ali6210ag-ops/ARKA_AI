from config.database import SessionLocal
from app.models import Supplier, Trader, TradeRequest


class ARKAMatchingEngine:

    def __init__(self):
        self.db = SessionLocal()


    def find_match(self, product_needed):

        suppliers = self.db.query(Supplier).all()

        results = []

        for supplier in suppliers:

            score = 0
            reasons = []


            # بررسی حوزه کاری
            if supplier.category:
                if "غذایی" in supplier.category or "مواد" in supplier.category:
                    score += 30
                    reasons.append("حوزه کاری مرتبط")


            # بررسی توضیحات
            if supplier.description:
                if product_needed in supplier.description:
                    score += 50
                    reasons.append("محصول مشابه")


            # بررسی شهر
            if supplier.city:
                score += 10
                reasons.append("اطلاعات مکانی موجود")


            results.append(
                {
                    "supplier": supplier.name,
                    "score": score,
                    "reasons": reasons
                }
            )


        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results



if __name__ == "__main__":

    engine = ARKAMatchingEngine()


    matches = engine.find_match(
        "عسل طبیعی"
    )


    print("=== ARKA AI Matching Result ===")


    for item in matches:

        print("--------------------")
        print("Supplier:", item["supplier"])
        print("Score:", item["score"], "%")
        print("Reasons:")

        for reason in item["reasons"]:
            print("-", reason)