#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        """
        Initialize Coffee object with size and price
        
        Args:
            size (str): Size of the coffee (Small, Medium, or Large)
            price (float): Price of the coffee
        """
        self._size = size
        self._price = price
    
    @property
    def size(self):
        """Get the size of the coffee"""
        return self._size
    
    @size.setter
    def size(self, value):
        """
        Set the size of the coffee
        Validates that the size is one of: Small, Medium, or Large
        """
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        self._size = value
    
    @property
    def price(self):
        """Get the price of the coffee"""
        return self._price
    
    @price.setter
    def price(self, value):
        """Set the price of the coffee"""
        self._price = value
    
    def tip(self):
        """
        Add a tip to the coffee
        Increases the price by 1 and prints a message
        """
        print("This coffee is great, here's a tip!")  # Using straight apostrophe
        self._price += 1