# Construct a class Circle that represents a Circle.


# The class should support the following functionalities:-
# perimeter() -> returns the perimeter of the circle
# area() -> returns the area of the circle


# Assume Π (pi) = 3.14 for calculations.
# You may define any properties in the class as you see appropriate.
class Circle:
    def __init__(self,x):
        self.r=x
    def perimeter(self):
        return 2*3.14*r
    def area(self):
        return 3.14*r**2
        
# a = new Circle(3)  // Radius = 3
# a.perimeter() // 18.84
# a.area() // 28.26
