#!usr/bin/env python3
# -*- coding: utf8 -*-
"""forms"""

from wtforms import(
    Form,
    StringField,
    FloatField,
    IntegerField,
    TextField,
    RadioField,
    validators
)
from app.database import Product

class ProductForm(Form):
    style = {'style': "width:100%"}
    name = StringField("Name", [validators.required(), validators.Length(min=4, max=45)],render_kw=style)

    price = FloatField("Price", [validators.required()], render_kw=style)
    quantity = IntegerField("Quantity", [validators.required()], render_kw=style)
    description = TextField("Description", [validators.required()], render_kw=style)
    instock = RadioField('In Stock', choices=[(1,'in stock'),(0,'Out of stock')])

class ReviewForm(Form):
    choices = Product.query.all()
    style = {'style': "width:100%"}
    product_name = StringField("Product Name", render_kw=style)
    reviewtext = TextField("Review Text", render_kw=style)
