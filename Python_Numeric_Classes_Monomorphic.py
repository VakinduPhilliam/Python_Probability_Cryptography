# Python Numeric Classes
# numbers — Numeric abstract base classes.
# The numbers module (PEP 3141) defines a hierarchy of numeric abstract base classes which progressively define more operations. None of the types 
# defined in this module can be instantiated.
# class numbers.Number 
# The root of the numeric hierarchy. If you just want to check if an argument x is a number, without caring what kind, use isinstance(x, Number).
#
# Because most of the operations on any given type will be very similar, it can be useful to define a helper function which generates the forward and
# reverse instances of any given operator.
#
# For example, fractions.Fraction uses:
# 

def _operator_fallbacks(monomorphic_operator, fallback_operator):

    def forward(a, b):

        if isinstance(b, (int, Fraction)):
            return monomorphic_operator(a, b)

        elif isinstance(b, float):
            return fallback_operator(float(a), b)

        elif isinstance(b, complex):
            return fallback_operator(complex(a), b)

        else:
            return NotImplemented

    forward.__name__ = '__' + fallback_operator.__name__ + '__'
    forward.__doc__ = monomorphic_operator.__doc__

    def reverse(b, a):

        if isinstance(a, Rational):

            # Includes ints.

            return monomorphic_operator(a, b)

        elif isinstance(a, numbers.Real):
            return fallback_operator(float(a), float(b))

        elif isinstance(a, numbers.Complex):
            return fallback_operator(complex(a), complex(b))

        else:
            return NotImplemented

    reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
    reverse.__doc__ = monomorphic_operator.__doc__

    return forward, reverse

def _add(a, b):
    """a + b"""

    return Fraction(a.numerator * b.denominator +
                    b.numerator * a.denominator,
                    a.denominator * b.denominator)

__add__, __radd__ = _operator_fallbacks(_add, operator.add)

# ...
