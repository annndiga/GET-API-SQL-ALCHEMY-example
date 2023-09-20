from app import db, app
from models import Product, Category, Review

# Initialize the app context to work with the database
app.app_context().push()

# Create categories
category1 = Category(name="Electronics")
category2 = Category(name="Clothing")
category3 = Category(name="Books")

# Create products
product1 = Product(
    title="Smartphone",
    price=499.99,
    description="A high-quality smartphone with advanced features.",
    image="https://example.com/smartphone.jpg",
    category=category1,
)

product2 = Product(
    title="Laptop",
    price=999.99,
    description="A powerful laptop for work and entertainment.",
    image="https://example.com/laptop.jpg",
    category=category1,
)

product3 = Product(
    title="T-shirt",
    price=19.99,
    description="A comfortable and stylish t-shirt.",
    image="https://example.com/tshirt.jpg",
    category=category2,
)

product4 = Product(
    title="Book - The Great Gatsby",
    price=12.99,
    description="A classic novel by F. Scott Fitzgerald.",
    image="https://example.com/book.jpg",
    category=category3,
)

# Create reviews
review1 = Review(associated_product=product1, text="Great smartphone!", rating=4.5)
review2 = Review(associated_product=product2, text="Excellent laptop!", rating=4.8)
review3 = Review(associated_product=product3, text="Very comfortable t-shirt.", rating=4.0)
review4 = Review(associated_product=product4, text="A timeless classic.", rating=4.7)



# Add objects to the session and commit to the database
db.session.add(category1)
db.session.add(category2)
db.session.add(category3)
db.session.add(product1)
db.session.add(product2)
db.session.add(product3)
db.session.add(product4)
db.session.add(review1)
db.session.add(review2)
db.session.add(review3)
db.session.add(review4)

db.session.commit()

print("Database seeded successfully.")
