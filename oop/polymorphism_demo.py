import math

class Shape:
    def area(self):
        """
        Base method meant to be overridden.
        Raises an error if a subclass does not override it.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Area of a rectangle = length × width"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Area of a circle = π × radius²"""
        return math.pi * (self.radius ** 2)