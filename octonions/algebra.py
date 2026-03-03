"""
Module for performing algebraic operations on octonions.
"""

import numpy as np

class Octonion:
    # Construct an Octonion with 8 float value componenets.
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


def multiply_octonions(o1, o2):
    # TODO: Multiplication rules.  
    print("Multiplying octonions in progress...")
    return Octonion(np.zeros(8))