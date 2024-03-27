import math

class Circle:
    def __init__(self, r):
        self.__radius = r
    
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return (math.pi) * (self.__radius ** 2)

    
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" , c1.area())

c2 = Circle(5)
print("Second circle radius:" , c2.getRadius())
print("Second circle area:" , c2.area())
