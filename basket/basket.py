

from random import random
from urllib import request


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('s_key')

        if 's_key' not in request.session:
            # sob request er same session ,,so we will get the same dictionary attached to the basket each request
            basket = self.session['s_key'] = {"total_qty": 0}

        self.basket = basket  # new basket create hobe but same dictionary of the current session attach hobe

    def add(self, product, product_qty):

        product_id = product.id

        print(type(product_id))
        if str(product_id) not in self.basket:
            self.basket[str(product_id)] = {"price": str(product.price), "qty": int(product_qty)}
            self.basket["total_qty"] = self.basket["total_qty"]+int(product_qty)

        else:

            self.basket[str(product_id)]["qty"] = int(self.basket[str(product_id)]["qty"])+int(product_qty)
            self.basket["total_qty"] = self.basket["total_qty"]+int(product_qty)

        self.session.modified = True  # to update session data in the database

        return self.basket["total_qty"]

    def get_total_qty(self):
        return self.basket["total_qty"]

    def keys(self):
        return list(self.basket.keys())

    def remove(self, id):
        self.basket["total_qty"] = self.basket["total_qty"]-self.basket[str(id)]["qty"]

        self.basket.pop(str(id), None)

        self.session.modified = True
