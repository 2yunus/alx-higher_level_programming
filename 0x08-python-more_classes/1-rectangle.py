#!/usr/bin/python3
class Rectangle:
        """Represent recangle"""
    def __init__(self, width=0, height=0):
        """"Initialize a new rectangle
        Args:
            size(int): The size of new rectangle
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        return self.width
    @property
    def height(self):
        return self.height
    @width.setter
    def width(self):
        if not isinstance(width,int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width 
    @height.setter
    def height(self):
         if not isinstance(height, int):
             raise TypeError("size must be an integer")
         elif width < 0:
             raise ValueError("size must be >= 0")
         self.__height = height
