from app.main import main
from flask import render_template
from app.models import Product

@main.route('/')
def index():
    """Homepage"""

    products = Product.query.limit(6).all()

    return render_template('main/index.html',products=products)

@main.route('/products')
def products():
    """Products listing page"""
    return "<h5>Products</h5>"