from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    serialize_rules = ('-products',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    products = db.relationship('Product', back_populates='category')

    def __repr__(self):
        return f'<Category {self.name}>'

class Review(db.Model):
    __tablename__ = 'reviews'

    serialize_rules = ('-product',)

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    text = db.Column(db.Text)
    rating = db.Column(db.Float)

   

    def __repr__(self):
        return f'<Review {self.text}>'

class Product(db.Model):
    __tablename__ = 'products'

    serialize_rules = ('-category',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    # Relationships with modified backref name
    category = db.relationship('Category', back_populates='products')
    reviews = db.relationship('Review', backref='associated_product', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Product {self.title}>'

