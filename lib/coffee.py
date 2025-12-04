#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):

        # create a "hidden" size variable
        self._size = None

        # use the property so the validation runs
        self.size = size

        # store the price (we assume it's a number)
        self.price = price

    # getter for size
    @property
    def size(self):
        return self._size

    # setter for size
    @size.setter
    def size(self, value):
        # only accept Small, Medium, or Large
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # tipping
    def tip(self):
        print("This coffee is great, here’s a tip!")
        # increase price by 1
        self.price += 1