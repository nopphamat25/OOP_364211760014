"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

#polymrphism with inhreitance
from math import  pi

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length =length
    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self,redius):
        self.redius = redius
    def area(self):
        return pi*(self.redius**2)
r = Rectangle(5.0,10.0)
c = Circle(7.7)

myshape = [r,c]

for x in myshape:
    print(x.area())