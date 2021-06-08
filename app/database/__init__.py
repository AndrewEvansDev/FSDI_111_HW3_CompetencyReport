#!usr/bin/env python3
# -*- coding: utf8 -*-
"""Database models"""


from app import db 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    instock = db.Column(db.Integer, nullable=True, default=1)
    reviews = db.relationship('Review', backref='product', lazy=True)

    def __repr__(self):
        return "<Product %r>" % self.name

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewtext = db.Column(db.Text, nullable=False)
    product_name = db.Column(db.String, db.ForeignKey('product.name'), nullable=False)
    
    def __repr__(self):
        return "<Review %r>" % self.name