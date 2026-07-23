from config.database import engine
from config.database import Base

from app.models import Product


print("Creating ARKA tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully ✅")