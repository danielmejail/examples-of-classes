class Rationals(object):
    def gcd(a,b):
        "a, b ints; this is the Euclidean algorithm"
        while (b > 0):
            r = a % b
            a = b
            b = r
        return a
    def lcm(a,b):
        return (a * b) // gcd(a,b)

class Ring(object):
    def __init__(self):
        pass
    def getZero(self):
        return self.zero
    def getOne(self):
        return self.one
    def getDescription(self):
        pass
    def __str__(self):
        return self.getDescription()

class RationalNumber(Rationals):
    def __init__(self, numerator, denominator):
        """
        numerator and denominator are ints;
        after successful initialisation, denominator is possitive and
        the pair (numerator, denominator) is primitive
        """
        if (denominator == 0):
            print("Denominator must be different from zero")
            raise ValueError
        else:
            if (denominator < 0):
                numerator = (-1) * numerator
                denominator = abs(denominator)
            g = Rationals.gcd(numerator, denominator)
            numerator //= g
            denominator //= g
            self.numerator = numerator
            self.denominator = denominator
    def __str__(self):
        s = str(self.numerator)
        if (self.denominator != 1):
            s += ('/' + str(self.denominator))
        return s
    def getNumerator(self):
        return self.numerator
    def getDenominator(self):
        return self.denominator
    def __eq__(self, other):
        return self.numerator * other.denominator - \
               self.denominator * other.numerator == 0
    def __lt__(self, other):
        return self.numerator * other.denominator - \
               self.denominator * other.numerator < 0
    def __add__(self, other):
        g = Rationals.gcd(self.denominator, other.denominator)
        denominator = (self.denominator * other.denominator) // g
        numerator = self.numerator * (other.denominator // g) + \
               (self.denominator // g) * other.numerator
        return RationalNumber(numerator, denominator)
    def __sub__(self, other):
        g = Rationals.gcd(self.denominator, other.denominator)
        denominator = (self.denominator * other.denominator) // g
        numerator = self.numerator * (other.denominator // g) - \
               (self.denominator // g) * other.numerator
        return RationalNumber(numerator, denominator)
    def __mul__(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        return RationalNumber(numerator, denominator)
    def __truediv__(self, other):
        if (other.numerator == 0):
            print("Cannot divide by zero")
            raise ZeroDivisionError
        denominator = self.denominator * other.numerator
        numerator = self.numerator * other.denominator
        return RationalNumber(numerator, denominator)
    def __neg__(self):
        return RationalNumber(-self.numerator, self.denominator)
    def __abs__(self):
        if (self.numerator < 0):
            return -self
        return self

class RingOfRationalNumbers(Rationals, Ring):
    # def __init__(self):
        # self.zero = RationalNumber(0,1)
    zero = RationalNumber(0,1)
        # self.one = RationalNumber(1,1)
    one = RationalNumber(1,1)
    def getDescription(self):
        return 'Ring of rational numbers'

x = RationalNumber(-6,-4)
y = RationalNumber(-12,45)
z = x / -y
QQ = RingOfRationalNumbers()
