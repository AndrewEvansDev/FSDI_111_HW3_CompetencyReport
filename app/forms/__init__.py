#!usr/bin/env python3
# -*- coding: utf8 -*-
"""forms"""

from wtforms import(
    Form,
    StringField,
    FloatField,
    IntegerField,
    TextField,
    validators
)


class ProductForm(Form):
    style = {'style': "width:100%"}
    name = StringField("Name", [validators.required(), validators.Length(min=4, max=45)],render_kw=style)

    price = FloatField("Price", [validators.required()], render_kw=style)
    quantity = IntegerField("Quantity", [validators.required()], render_kw=style)
    description = TextField("Description", [validators.required()], render_kw=style)