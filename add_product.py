from config.database import SessionLocal
from app.models import Product


db = SessionLocal()


product = Product(
    name="کره شمال",
    category="مواد غذایی",
    supplier="ARCKA",
    buy_price=100000,
    sell_price=120000,
    quantity=500,
    description="محصول تستی ARKA"
)


db.add(product)
db.commit()
db.refresh(product)


print("Product Added ✅")
print(product.id)
print(product.name)


db.close()