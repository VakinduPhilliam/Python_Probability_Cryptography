# Python Numeric Classes
# numbers — Numeric abstract base classes.
# The numbers module (PEP 3141) defines a hierarchy of numeric abstract base classes which progressively define more operations. None of the types
# defined in this module can be instantiated.
# class numbers.Number 
# The root of the numeric hierarchy. If you just want to check if an argument x is a number, without caring what kind, use isinstance(x, Number).
#
# Notes for type implementors:
# 
# Implementors should be careful to make equal numbers equal and hash them to the same values.
# This may be subtle if there are two different extensions of the real numbers.
#
# For example, fractions.Fraction implements hash() as follows:
# 

def __hash__(self):

    if self.denominator == 1:

        # Get integers right.

        return hash(self.numerator)

    # Expensive check, but definitely correct.

    if self == float(self):
        return hash(float(self))

    else:

        # Use tuple's hash to avoid a high collision rate on
        # simple fractions.

        return hash((self.numerator, self.denominator))
 
#
# Adding More Numeric ABCs:
# 
# There are, of course, more possible ABCs for numbers, and this would be a poor hierarchy if it precluded the possibility of adding those.
# You can add MyFoo between Complex and Real with:
# 

class MyFoo(Complex): 

# ...

MyFoo.register(Real)
 
#
# Implementing the arithmetic operations:
# 
# We want to implement the arithmetic operations so that mixed-mode operations either call an implementation whose author knew about the types of
# both arguments, or convert both to the nearest built in type and do the operation there. For subtypes of Integral, this means that __add__() 
# and __radd__() should be defined as:
# 

class MyIntegral(Integral):

    def __add__(self, other):

        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)

        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(self, other)

        else:
            return NotImplemented

    def __radd__(self, other):

        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)

        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(other, self)

        elif isinstance(other, Integral):
            return int(other) + int(self)

        elif isinstance(other, Real):
            return float(other) + float(self)

        elif isinstance(other, Complex):
            return complex(other) + complex(self)

        else:
            return NotImplemented
