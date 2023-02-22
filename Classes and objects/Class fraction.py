# Construct a class Fraction which stores a fraction. It should contain the

# -Numerator
# -Denominator

# Assume denominator will never be 0.

# The class should support the following functionalities

# add(Fraction) -> Returns the sum of two fractions

# subtract(Fraction) -> Returns the difference of two fractions

# multiply(Fraction) -> Returns the product of two fractions

# The fraction returned needs to be in the simplest form. If the fraction is p/q then p and q must be co-prime.

# You may define any properties in the class as you see appropriate.

class Fraction:
    Numerator=0
    Denominator=0

    def gcd(self,n,d):
        if d==0:
            return abs(n)
        else:
            return self.gcd(d,n%d)

    def __init__(self,numerator=0,denominator=0):
        self.numerator=numerator
        self.denominator=denominator

    def add(self, a):
        Numerator=self.numerator*a.denominator + self.denominator*a.numerator
        Denominator=self.denominator*a.denominator
        k=self.gcd(abs(Numerator),abs(Denominator))
        Numerator=Numerator//k
        Denominator=Denominator//k
        return Fraction(Numerator,Denominator)
    
    def subtract(self,a):
        Numerator=self.numerator*a.denominator - self.denominator*a.numerator
        Denominator=self.denominator*a.denominator
        k=self.gcd(abs(Numerator),abs(Denominator))
        Numerator=Numerator//k
        Denominator=Denominator//k
        return Fraction(Numerator,Denominator)
    
    def multiply(self, a):
        Numerator=self.numerator*a.numerator
        Denominator=self.denominator*a.denominator
        k=self.gcd(abs(Numerator),abs(Denominator))
        Numerator=Numerator//k
        Denominator=Denominator//k
        return Fraction(Numerator,Denominator)
    
        
# Fraction x = new Fraction(2, 3)  // 2/3
# Fraction y = new Fraction(4, 5) // 4/5
# Fraction z = x.add(y) // 22/15
# Fraction z = x.subtract(y) // -2/15
# Fraction z = x.multiply(y) // 8/15
