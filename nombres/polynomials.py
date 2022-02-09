class UnivariatePolynomialRing(object):
    def __init__(self, indeterminate, base_ring = float):
        """
        indeterminate is a str representing the variable
        base_ring is a type : int, float or an instance of
        UnivariatePolynomialRing
        """
        self.base_ring = base_ring
        self.indeterminate = indeterminate
        self.zero = UnivariatePolynomial(self,[])
    def getBaseRing(self):
        return self.base_ring
    def getIndeterminate(self):
        return self.indeterminate
    def getZero(self):
        return self.zero
    def __str__(self):
        return "Univariate polynomial ring with indeterminate " + \
               self.indeterminate + " over " + str(K.getBaseRing())
    def __eq__(self, other):
        if (self.base_ring != other.base_ring):
            return False
        if (self.indeterminate != other.indeterminate):
            return False
        return True    
    def gcd(self,f,g):
        """
        f and g are assumed to belong to the class of polynomials
        with coefficients in the ring self
        """
        a = f
        b = g
        while not (b.isZero()):
            r = a.mod(b)
            a = b
            b = r
        return a

class UnivariatePolynomial(UnivariatePolynomialRing):
    def __init__(self, polynomial_ring, coefficients):
        """
        polynomial_ring : UnivariatePolynomialRing
        coefficients : a list containing the coefficients ordered from
        constant term up to leading term, objects of type
        polynomial_ring.base_ring
        """
        self.polynomial_ring = polynomial_ring
        highest = -1
        i = len(coefficients) - 1
        while (i >= 0 and highest < 0):
            if (coefficients[i] != 0):
                highest = i
            i -= 1
        self.coefficients = coefficients[:highest+1]
        if highest >= 0:
            self.degree = highest
    def getCoefficients(self):
        return self.coefficients[:]
    def getPolynomialRing(self):
        return self.polynomial_ring
    def isZero(self):
        if (len(self.coefficients) == 0):
            return True
        return False
    def getDegree(self):
        if (self.isZero()):
            print("the degree of the zero polynomial is undefined")
            raise AttributeError
        return self.degree
    def getLeadingTerm(self):
        if (self.isZero()):
            return 0
            # this should be replaced by the zero element in
            # the ring of coefficients
        return self.coefficients[-1]
    def getConstantTerm(self):
        if (self.isZero()):
            return 0
            # this should be replaced by the zero element in
            # the ring of coefficients
        return self.coefficients[0]
    def evaluate(self, x):
        """
        x : an int; it should be an element of the coefficient ring
        """
        tot = self.polynomial_ring.base_ring.zero
        i = self.getDegree()
        while (i >= 0):
            tot = tot * x + self.coefficients[i]
            i -= 1
        return tot
    """
    def __lt__(self,other):
        if self.isZero():
            return not other.isZero()
        if other.isZero():
            return True
        return self.degree < other.degree
    """
    def derivative(self):
        if (self.isZero()):
            return self.polynomial_ring.getZero()
        coefficients = self.coefficients
        derived = []
        for i in range(self.degree):
            derived.append((i+1) * coefficients[i+1])
        return UnivariatePolynomial(self.polynomial_ring, derived)
    def mod(self,other):
        """returns remainder of self after division by other"""
        if (other.isZero()):
            print("Cannot divide by zero")
            raise ValueError
        r = self
        while not (r.isZero() or r.degree < other.degree):
            c = UnivariateMonomial(r.polynomial_ring,
                                   r.degree - other.degree,
                                   r.getLeadingTerm() / other.getLeadingTerm())
            r = r - c * other
        return r
    def __add__(self,other):
        if (self.polynomial_ring != other.polynomial_ring):
            print("Cannot add polynomials belonging to different rings")
            raise ValueError
        if (self.isZero()):
            return other
        if (other.isZero()):
            return self
        i = 0
        coefficients = []
        while (i <= min(self.degree,other.degree)):
            coefficients.append(self.coefficients[i] + other.coefficients[i])
            i += 1
        while (i <= self.degree):
            coefficients.append(self.coefficients[i])
            i += 1
        while (i <= other.degree):
            coefficients.append(other.coefficients[i])
            i += 1
        return UnivariatePolynomial(self.polynomial_ring, coefficients)
    def __sub__(self,other):
        if (self.polynomial_ring != other.polynomial_ring):
            print("Cannot subtract polynomials belonging to different rings")
            raise ValueError
        if (self.isZero()):
            return other
        if (other.isZero()):
            return self
        i = 0
        coefficients = []
        while (i <= min(self.degree,other.degree)):
            coefficients.append(self.coefficients[i] - other.coefficients[i])
            i += 1
        while (i <= self.degree):
            coefficients.append(self.coefficients[i])
            i += 1
        while (i <= other.degree):
            coefficients.append(-1 * other.coefficients[i])
            i += 1
        return UnivariatePolynomial(self.polynomial_ring, coefficients)
    def __mul__(self,other):
        if (self.polynomial_ring != other.polynomial_ring):
            print("Cannot multiply polynomials belonging to different rings")
            raise ValueError
        if (self.isZero() or other.isZero()):
            return self.polynomial_ring.getZero()
        k = 0
        coefficients = []
        while (k <= self.degree + other.degree):
            sum_of_products = 0
            i = 0
            while (i <= k):
                if (i <= self.degree and (k - i) <= other.degree):
                    sum_of_products += self.coefficients[i] * \
                                       other.coefficients[k-i]
                i += 1
            coefficients.append(sum_of_products)
            k += 1
        return UnivariatePolynomial(self.polynomial_ring, coefficients)
    def __eq__(self,other):
        if (self.polynomial_ring != other.polynomial_ring):
            print("Cannot compare polynomials belonging to different rings")
            raise ValueError
        if (self.isZero()):
            return other.isZero()
        if (other.isZero()):
            return False
        if self.degree != other.degree:
            return False
        i = 0
        while (i <= self.degree):
            if (self.coefficients[i] != other.coefficients[i]):
                return False
            i += 1
        return True
    def __str__(self):
        if (self.isZero()):
            return '0'
        representation = ''
        for i in range(self.degree):
            representation += str(self.coefficients[i]) + '*' + \
                              (self.polynomial_ring).getIndeterminate() + \
                              '^' + str(i) + ' + '
        representation += str(self.coefficients[-1]) + '*' + \
                              (self.polynomial_ring).getIndeterminate() + \
                              '^' + str(self.degree)
        return representation

class UnivariateMonomial(UnivariatePolynomial):
    def __init__(self, polynomial_ring, degree, coefficient):
        """assumes degree >= 0, i.e. the monomial is not zero"""
        coefficients = []
        for i in range(degree):
            coefficients.append(0)
        coefficients.append(coefficient)
        # UnivariatePolynomial.__init__(self,polynomial_ring,coefficients)
        self.coefficients = coefficients
        self.polynomial_ring = polynomial_ring
        self.degree = degree


# class ConstantPolynomial(UnivariateMonomial):

from rationals import *
K = UnivariatePolynomialRing("T",QQ)
print(K)

R = UnivariatePolynomialRing("S")
A = UnivariatePolynomialRing("T")

print(K == R)
print(K == A)
A = UnivariatePolynomialRing("T",QQ)
print(K == A)

f = UnivariatePolynomial(K, [-1,-1,3,1,-3,3,0,-4,2,0,-1,1])
"""
g = f.derivative()
"""
h = UnivariatePolynomial(K,[RationalNumber(4,5),RationalNumber(-7,3), \
                            RationalNumber(2,1)])
print('h = ' + str(h))

x = RationalNumber(3,-1)
print('h(' + str(x) + ') = ' + str(h.evaluate(x)))
x = RationalNumber(3,5)
print('h(' + str(x) + ') = ' + str(h.evaluate(x)))
