from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.admin import admin
from app.models import Product


@admin.route('/')
@login_required
def dashboard():
    """Admin dashboard"""
    
    # Get statistics
    total_products = Product.query.count()
    anime_count = Product.query.filter_by(category='anime').count()
    stationery_count = Product.query.filter_by(category='stationery').count()
    low_stock = Product.query.filter(Product.stock < 5).count()
    out_of_stock = Product.query.filter(Product.stock == 0).count()
    
    # Get recent products
    recent_products = Product.query.order_by(Product.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_products=total_products,
                         anime_count=anime_count,
                         stationery_count=stationery_count,
                         low_stock=low_stock,
                         out_of_stock=out_of_stock,
                         recent_products=recent_products)

@admin.route('/products')
@login_required
def products_list():
    """List all products for admin"""
    products = Product.query.order_by(Product.created_at.desc()).all()
    return render_template('admin/products_list.html', products=products)


@admin.route('/add-product')
@login_required
def add_product():
    """Add new product form"""
    # We'll implement this fully in the next session
    return "<h1>Add Product Form - Coming Soon!</h1><a href='/admin/'>← Back to Dashboard</a>"