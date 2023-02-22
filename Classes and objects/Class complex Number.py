# Construct a class called ComplexNumber which stores two properties

# real - The real part
# imaginary - The imaginary part

# The name of the properties should be strictly real and imaginary


# Implement the following functionalities inside this class :-

# add(ComplexNumber) -> Returns an object of ComplexNumber having sum of the two complex numbers.

# subtract(ComplexNumber) -> Returns an object of ComplexNumber having difference of the two complex numbers.

# multiply(ComplexNumber) -> Returns an object of ComplexNumber having multiplication of the two complex numbers.

# divide(ComplexNumber) -> Returns an object of ComplexNumber having division of the two complex numbers.

class ComplexNumber:
    real=0
    imaginary=0
    # Define constructor here
    def __init__(self,a,b):
        self.real=a
        self.imaginary=b


    def add(self, x: "ComplexNumber"):
        m=x.real+self.real
        n=x.imaginary+self.imaginary
        return ComplexNumber(m,n)
    
    
    def subtract(self, x: "ComplexNumber")->"ComplexNumber":
        m=self.real-x.real
        n=self.imaginary-x.imaginary
        return ComplexNumber(m,n)
        
        
    def multiply(self, x: "ComplexNumber")->"ComplexNumber":
        m=(x.real*self.real-x.imaginary*self.imaginary)
        n=(self.real*x.imaginary+self.imaginary*x.real)
        return ComplexNumber(m,n)
    
    
    def divide(self, x: "ComplexNumber")->"ComplexNumber":
        m= ((self.real*x.real)+(self.imaginary*x.imaginary))/((x.real)**2 +(x.imaginary)**2)
        n= ((self.imaginary*x.real)-(self.real*x.imaginary))/((x.real)**2 +(x.imaginary)**2)
        return ComplexNumber(m,n)
    
        
# ComplexNumber a = new ComplexNumber(10, 5)
# ComplexNumber b = new ComplexNumber(2, 3)
# ComplexNumber c1 = a.add(b) 
# ComplexNumber c2 = a.subtract(b)
# ComplexNumber c3 = a.multiply(b)
# ComplexNumber c4 = a.divide(b)