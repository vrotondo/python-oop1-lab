#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        """
        Initialize Book object with title and page count
        
        Args:
            title (str): The title of the book
            page_count (int): The number of pages in the book
        """
        self._title = title
        self._page_count = page_count
    
    @property
    def title(self):
        """Get the title of the book"""
        return self._title
    
    @title.setter
    def title(self, value):
        """Set the title of the book"""
        self._title = value
    
    @property
    def page_count(self):
        """Get the page count of the book"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Set the page count of the book
        Validates that the page count is an integer
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value
    
    def turn_page(self):
        """
        Turn the page in the book
        Prints a message when a page is turned
        """
        print("Flipping the page...wow, you read fast!")