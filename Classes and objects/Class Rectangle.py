# Construct a class Rectangle that represents a rectangle.
# The class should support the following functionalities:-
# perimeter() -> returns the perimeter of the rectangle
# area() -> returns the area of the rectangle
# You may define any properties in the class as you see appropriate.

class Rectangle:
    l=0
    b=0
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def perimeter(self):
        return 2*(self.l+self.b) 
    def area(self):
        return self.l*self.b
    
        
# Rectangle a = new Rectangle(2, 3)  // Length = 2, Breadth = 3
# a.perimeter() // Should give 10
# a.area() // Should give 6