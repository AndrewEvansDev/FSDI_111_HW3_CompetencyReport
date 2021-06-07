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
    create_product("Papayas",12.99,159)
    create_product("Tangerines",5.99,99)
    create_product("Mangos", 3.5, 42)
    create_product("Nectarines", 3.5, 42)
    create_product("Bananas",2.99,1539)
    create_product("Oranges",4.99,99)
    create_product("Pears", 4.2, 420)
    create_product("Strawberries", 5.5, 42)
    


    products = Product.query.all()
    print(products)