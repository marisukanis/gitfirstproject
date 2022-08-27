"""
Inheritance:
    - inheriting attributes and methods from the base/parent class
    - derived/child class , which can have its own attributes and methods

class <<ChildClassName>>(BaseClass):
    def __init__(self):
        super().__init__(self)

class <<ChildClassName>>(BaseClass):
    def __init__(self):
        BaseClass().__init__(self)
"""
"""
class rectangle:
- attributes 'len' and 'breadth'
- methods - perimeter, area

child class = Parallogram
- inherits from rectangle
- attributes = heights
- volume
"""

class Rectangle:    #creating a class
    def __init__(self, len = 5, brd = 6):
        self.length = len
        self.breadth = brd

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

    def show(self):
        print(f"Rectangle Info:\n"
              f"length: {self.length}\n"
              f"breadth: {self.breadth}\n"
              f"Area: {self.area}\n"
              f"Perimeter: {self.perimeter()}")


class Parallelogram(Rectangle):
    def __init__(self, len, brd, height):
        super().__init__(len, brd)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height  #volume formula

    #@classmethod
    #def show(cls):
       # cls.show()

    def show(self):
        print(f"Parallelogram Info:\n"
              f"length: {self.length}\n"
              f"breadth: {self.breadth}\n"
              f"Area: {self.area()}\n"
              f"Perimeter: {self.perimeter()}\n"
              f"Volume: {self.volume()}")

rect1 = Rectangle (10, 8)
rect1.show()

para1 = Parallelogram(10, 8, 4)
para1.show()