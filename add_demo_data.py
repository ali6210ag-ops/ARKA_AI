from config.database import SessionLocal
from app.models import Supplier, Product


db = SessionLocal()


suppliers = [

    Supplier(
        name="خشکبار پارس",
        category="مواد غذایی خشکبار",
        city="تهران",
        phone="09120000001",
        description="تامین کننده پسته، بادام، گردو، خشکبار صادراتی"
    ),


    Supplier(
        name="شرکت عسل زاگرس",
        category="مواد غذایی",
        city="کرمانشاه",
        phone="09120000002",
        description="تولید کننده عسل طبیعی، عسل کوهی، محصولات زنبور عسل"
    ),


    Supplier(
        name="فولاد آریا",
        category="صنعت و فلزات",
        city="اصفهان",
        phone="09120000003",
        description="تامین فولاد، میلگرد، ورق فولادی، آهن آلات"
    ),


    Supplier(
        name="پتروشیمی پارس",
        category="مواد صنعتی",
        city="بوشهر",
        phone="09120000004",
        description="تامین مواد پتروشیمی، پلیمر و محصولات صنعتی"
    ),


    Supplier(
        name="برنج شمال ایرانیان",
        category="مواد غذایی",
        city="گیلان",
        phone="09120000005",
        description="تامین برنج ایرانی، برنج طارم، برنج صادراتی"
    ),


    Supplier(
        name="زعفران طلایی",
        category="مواد غذایی",
        city="مشهد",
        phone="09120000006",
        description="تولید و صادرات زعفران، ادویه و محصولات کشاورزی"
    ),


]


for supplier in suppliers:

    db.add(supplier)


db.commit()


db.close()


print("Demo suppliers added successfully")