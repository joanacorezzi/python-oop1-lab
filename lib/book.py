#!/usr/bin/env python3

class Book:
        def __init__(self, title, page_count):

        #Initialize a new Book object
        # store the title normally
            self.title = title

        # create a private variable for page_count
            self._page_count = None

        # use the setter so validation happens
            self.page_count = page_count

    # getter for page_count
        @property

        def page_count(self):
            return self._page_count

    # setter for page_count
        @page_count.setter
        def page_count(self, value):
        # check if the value is an integer
            if isinstance(value, int):
                self._page_count = value
            else:
                print("page_count must be an integer")

    # turn the page
        def turn_page(self):
            print("Flipping the page...wow, you read fast!")
    
        