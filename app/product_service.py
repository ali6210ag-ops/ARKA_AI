from config.database import SessionLocal
from app.models import Product


class ProductService:

    def add_product(
        self,
        name,
        category,
        supplier,
        buy_price,
        sell_price,
        quantity,
        description=""
    ):

        db = SessionLocal()

        product = Product(
            name=name,
            category=category,
            supplier=supplier,
            buy_price=buy_price,
            sell_price=sell_price,
            quantity=quantity,
            description=description
        )

        db.add(product)
        db.commit()
        db.refresh(product)

        db.close()

        return product


    def get_products(self):

        db = SessionLocal()

        products = db.query(Product).all()

        db.close()

        return products