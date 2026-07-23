from app.product_service import ProductService


service = ProductService()


products = service.get_products()


for product in products:
    print(
        product.id,
        product.name,
        product.quantity
    )