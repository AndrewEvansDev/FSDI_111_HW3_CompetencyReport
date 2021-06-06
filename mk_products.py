#!usr/bin/env python3
# -*- coding: utf8 -*-
"""creating initial products db"""
from app import db
from app.database import Product


def create_product(name, price, quantity):
    """
    Creates sample products
    """

    db.session.add(
        Product(
            name=name,
            price=price,
            quantity=quantity
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_product("bananas",23.23,12)
    create_product("oranges",12.23,50)
    create_product("Mangos", 42.42, 42)
    products = Product.query.all()
    print(products)