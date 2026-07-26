from config.database import SessionLocal
from app.models import Supplier


class ARKAMatchingEngine:

    def __init__(self):
        self.db = SessionLocal()


    def find_match(self, product_needed):

        suppliers = self.db.query(Supplier).all()

        results = []

        product = product_needed.strip().lower()


        product_rules = {

            "فولاد": {
                "keywords": [
                    "فولاد",
                    "ورق",
                    "آهن",
                    "میلگرد"
                ],
                "category": [
                    "صنعت",
                    "فلز"
                ]
            },


            "پسته": {
                "keywords": [
                    "پسته",
                    "بادام",
                    "گردو",
                    "خشکبار"
                ],
                "category": [
                    "غذایی",
                    "خشکبار"
                ]
            },


            "عسل": {
                "keywords": [
                    "عسل",
                    "زنبور",
                    "طبیعی"
                ],
                "category": [
                    "غذایی"
                ]
            },


            "برنج": {
                "keywords": [
                    "برنج",
                    "طارم",
                    "کشاورزی"
                ],
                "category": [
                    "غذایی",
                    "کشاورزی"
                ]
            },


            "پلیمر": {
                "keywords": [
                    "پلیمر",
                    "پلاستیک"
                ],
                "category": [
                    "صنعت",
                    "مواد"
                ]
            }

        }



        rule = product_rules.get(

            product,

            {
                "keywords": [product],
                "category": []
            }

        )



        for supplier in suppliers:


            score = 0
            reasons = []


            text = (

                (supplier.name or "")
                +
                (supplier.description or "")

            ).lower()



            # تطبیق محصول

            if any(

                word in text

                for word in rule["keywords"]

            ):

                score += 60

                reasons.append(
                    "محصول دقیقاً مرتبط"
                )



            # تطبیق دسته کاری

            if supplier.category:

                if any(

                    cat in supplier.category

                    for cat in rule["category"]

                ):

                    score += 20

                    reasons.append(
                        "حوزه کاری مرتبط"
                    )



            # اطلاعات کامل

            if supplier.city and supplier.phone:

                score += 10

                reasons.append(
                    "اطلاعات تامین‌کننده کامل"
                )



            # فقط نتایج قابل قبول

            if score >= 30:

                results.append(

                    {
                        "supplier": supplier.name,

                        "score": score,

                        "reasons": reasons

                    }

                )



        # مرتب‌سازی امتیاز

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )



        # حذف تکراری‌ها

        unique = []

        names = set()



        for item in results:

            if item["supplier"] not in names:

                unique.append(item)

                names.add(item["supplier"])



        return unique[:5]