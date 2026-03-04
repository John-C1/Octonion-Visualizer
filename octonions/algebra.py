"""
algebra.py

Provides an implementation of the Octonion algebra using the Cayley-Dickson construction.

The Octonion class allows for:
- Addition, subtraction, and multiplication (non-associative) of octonions.
- Conjugation and norm calculation.

Octonions are represented with 8 real components.
"""

import numpy as np

class Octonion:
    """
    Represents an octonion of the form x0 + x1e1 + x2e2 ... + x7e7
    where xi are real numbers.

    Octonion multipication is defined using the Cayley-Dickson construction.
    Octonion algebra is alternative, but not associative, i.e. (ab)c != a(bc) in general.
    """
    def __init__(self, components):
        if len(components) != 8:
            raise ValueError("Must have 8 components.")
        self.components = np.array(components, dtype=float)

    def __add__(self, other):
        if not isinstance(other, Octonion):
            raise ValueError("Must add two Octonions.")
        return Octonion(self.components + other.components)

    def __mul__(self, other):
        return multiply_octonions(self, other)

    def __eq__(self, other):
        if not isinstance(other, Octonion):
            raise ValueError("Octonion must be compared with another Octonion.")
        return np.allclose(self.components, other.components)

    def __sub__(self, other):
        if not isinstance(other, Octonion):
            raise ValueError("Must subtract two Octonions.")
        return Octonion(self.components - other.components)
    
    def __repr__(self): 
        return f"Octonion(x0: {self.components[0]}, x1: {self.components[1]}, \
                          x2: {self.components[2]}, x3: {self.components[3]}, \
                          x4: {self.components[4]}, x5: {self.components[5]}, \
                          x6: {self.components[6]}, x7: {self.components[7]})"

    def conjugate(self):
        # A conjugate of an octonion flips the sign of all imaginary comopnents.
        return Octonion([self.components[0], -self.components[1], -self.components[2], 
                         -self.components[3], -self.components[4], -self.components[5], 
                         -self.components[6], -self.components[7]])
    
    def norm(self): 
        # Norm definition used here is the Euclidian distance formula.
        return np.sqrt(np.sum(self.components ** 2))


def multiply_octonions(o1, o2):
    # TODO: Multiplication rules.  
    print("Multiplying octonions in progress...")
    return Octonion(np.zeros(8))