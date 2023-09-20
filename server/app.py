from flask import Flask, jsonify,make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product, Category, Review

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Products/Review API"

# Routes for Categories

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    category_list = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify(category_list)

@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Category name is required'}), 400

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully'}), 201

@app.route('/categories/<int:id>', methods=['GET'])
def get_category_by_id(id):
    category = Category.query.filter_by(id=id).first()

    if category is None:
        return jsonify({'error': 'Category not found'}), 404

    category_dict = {
        "name": category.name,
        "description": category.description,
    }

    response = make_response(
        jsonify(category_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response 

# Routes for Products

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []

    for product in products:
        product_list.append({
            'id': product.id,
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'image': product.image,
            'category_id': product.category_id,
        })

    return jsonify(product_list)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    title = data.get('title')
    price = data.get('price')
    description = data.get('description')
    image = data.get('image')
    category_id = data.get('category_id')

    if not title or not price or not description or not image or not category_id:
        return jsonify({'message': 'All fields are required'}), 400

    product = Product(title=title, price=price, description=description, image=image, category_id=category_id)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@app.route('/product/<int:id>', methods=['GET'])
def get_product_by_id(id):
     product = Product.query.get(product_id)
     if product is None:
        return jsonify({'message': 'Product not found'}), 404

    # Create a dictionary for the product, including the category information
     product_dict = {
        'id': product.id,
        'title': product.title,
        'price': product.price,
        'description': product.description,
        'image': product.image,
        'category': {
            'id': product.category.id,
            'name': product.category.name
        },
        'reviews': []  
    }

     return jsonify(product_dict)

    

# Routes for Reviews

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    review_list = []

    for review in reviews:
        review_list.append({
            'id': review.id,
            'product_id': review.product_id,
            'text': review.text,
            'rating': review.rating,
        })

    return jsonify(review_list)

@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    product_id = data.get('product_id')
    text = data.get('text')
    rating = data.get('rating')

    if not product_id or not text or not rating:
        return jsonify({'message': 'All fields are required'}), 400

    review = Review(product_id=product_id, text=text, rating=rating)
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

@app.route('/reviews/<int:id>', methods=['GET'])
def get_review_by_id(id):
    review = Review.query.filter_by(id=id).first()

    if review is None:
        return jsonify({'error': 'Review not found'}), 404

    review_dict = {
        "title": review.title,
        "rating": review.rating,
        "comment": review.comment,
    }

    response = make_response(
        jsonify(review_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)