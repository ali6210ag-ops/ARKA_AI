from app.models import Supplier, Trader, TradeRequest
from config.database import SessionLocal


db = SessionLocal()


print("=== ARKA B2B Matching Test ===")


# ساخت تامین کننده
supplier = Supplier(
    name="شرکت عسل زاگرس",
    category="مواد غذایی",
    city="تبریز",
    phone="09120000000",
    description="تولید کننده عسل طبیعی"
)


db.add(supplier)


# ساخت تاجر
trader = Trader(
    name="بازرگانی خلیج",
    company="Gulf Trading",
    city="دبی",
    phone="09220000000",
    description="خریدار محصولات غذایی"
)


db.add(trader)


# درخواست خرید
request = TradeRequest(
    trader_name="بازرگانی خلیج",
    product_needed="عسل طبیعی",
    quantity=5000,
    budget=200000000
)


db.add(request)


db.commit()


print("Supplier Added:")
print(supplier.name)


print("Trader Added:")
print(trader.name)


print("Request Added:")
print(request.product_needed)


db.close()