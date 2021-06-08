#!usr/bin/env python3
# -*- coding: utf8 -*-
"""Route definitions"""

from flask import (
    render_template,
    request,
    redirect,
    url_for, flash
    )
from werkzeug.utils import redirect
from app import app, db
from datetime import datetime
from app.database import Product, Review
from app.forms import ProductForm, ReviewForm


@app.route("/")
@app.route("/home")
def index():
    version = {
        "ok": True,
        "message": "success",
        "version": "1.0.0",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return render_template("index.html", version=version)

    
@app.route("/products") #new
def get_products():
    """retrieve and display all products"""
    products = Product.query.all()
    return render_template("product_list.html", product_list=products)


@app.route("/outofstock") #new
def products_outofstock():
    """retrieve and display all out of stock products"""
    products = Product.query.all()
    return render_template("products_outofstock.html", product_list=products)


@app.route("/products/<int:pid>")
def get_product_detail(pid):
    """retrieve and display a single product"""  
    product = Product.query.filter_by(id=pid).first()
    return render_template("product_detail.html", product=product)


@app.route("/products/<int:pid>", methods=["POST"])
def update_product(pid):
    form = ProductForm(request.form)
    if form.validate():
        product = Product.query.filter_by(id=pid).first()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        product.instock = form.instock.data
        db.session.commit()
        flash("Product updated!")
        return redirect(url_for('get_products'))
    # if validations don't pass, form now we'll just also redirect
    # to get_products:
    flash("Invalid data")
    return redirect(url_for('get_products'))


@app.route("/products/modifications/<int:pid>")
def update_product_form(pid):
    form = ProductForm()
    product = Product.query.filter_by(id=pid).first()
    return render_template("update_form.html", form=form, product=product)


@app.route("/products/registrations")
def create_product_form():
    """Renders the create product form"""
    prod_form = ProductForm()
    return render_template("create_form.html", form=prod_form)


@app.route("/products", methods=["POST"])
def create_product():
    """Create a new product"""
    form = ProductForm(request.form)
    if form.validate():
        product = Product()
        product.name = form.name.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        product.description = form.description.data
        product.instock = form.instock.data
        db.session.add(product)
        db.session.commit()
        flash("Product created!")
        return redirect(url_for('get_products'))
    flash("Invalid data")
    return redirect(url_for('get_products'))


@app.route("/reviews")
def display_reviews():
    """retrieve and display all product reviews"""
    reviews = Review.query.all()
    return render_template("reviews.html", reviews_list=reviews)

@app.route("/reviews", methods=["POST"])
def create_review():
    """Create product review"""
    form = ReviewForm(request.form)
    if form.validate():
        review = Review()
        review.reviewtext = form.reviewtext.data
        review.product_name = form.product_name.data
        db.session.add(review)
        db.session.commit()
        flash("Review added")
        return redirect(url_for('display_reviews'))
    flash("Invalid data")
    return redirect(url_for('display_reviews'))

@app.route("/reviews/registrations")
def create_review_form():
    """Renders the create product form"""
    Review_form = ReviewForm()
    return render_template("review_form.html", form=Review_form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
