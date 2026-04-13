"""
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
        return f"{self.components[0]}, {self.components[1]}i, {self.components[2]}j, {self.components[3]}k, {self.components[4]}l, {self.components[5]}li, {self.components[6]}lj, {self.components[7]}lk"

    def conjugate(self):
        # A conjugate of an octonion flips the sign of all imaginary comopnents.
        return Octonion([self.components[0], -self.components[1], -self.components[2], 
                         -self.components[3], -self.components[4], -self.components[5], 
                         -self.components[6], -self.components[7]])
    
    def norm(self): 
        # Norm definition used here is the Euclidian distance formula.
        return np.sqrt(np.sum(self.components ** 2))


def multiply_octonions(o1, o2):
    # Octonion multiplication (a,b)(c,d) = (ac - d*b, da + bc*) where a,b,c,d are Quaternions.
    a, b = to_quaternion_pair(o1)
    c, d = to_quaternion_pair(o2)
    c_conj = quaternion_conjugate(c)
    d_conj = quaternion_conjugate(d)
    ac = multiply_quaternions(a, c)
    d_conjb = multiply_quaternions(d_conj,b)
    da = multiply_quaternions(d,a)
    bc_conj = multiply_quaternions(b, c_conj)

    result = Octonion(np.concatenate((ac - d_conjb, da + bc_conj)))
    return result

   
def quaternion_conjugate(q):
    # Conjugate of quaternion (a,b)* = (a*, -b) where a, b are complex numbers.
    if q.shape != (4,):
        raise ValueError("Quaternion must have 4 components.")
    return np.array([q[0], -q[1], -q[2], -q[3]])


def to_quaternion_pair(octonion):
    # Must represent octonions as quaternion pair to multiply them.
    a = octonion.components[:4]
    b = octonion.components[4:]
    return a, b


def multiply_quaternions(q1, q2):
    # Quaternion multiplication (a,b)(c,d) = (ac - d*b, da + bc*) where a,b,c,d are complex numbers.
    if (q1.shape != (4,)) or (q2.shape != (4,)):
        raise ValueError("Quaternions must have 4 components.")
    
    a = np.array(q1[:2])
    b = np.array(q1[2:])
    c = np.array(q2[:2])
    d = np.array(q2[2:])
    c_conj = np.array([c[0], -c[1]])
    d_conj = np.array([d[0], -d[1]])

    ac = multiply_complex(a, c)
    d_conjb = multiply_complex(d_conj, b)
    da = multiply_complex(d, a)
    bc_conj = multiply_complex(b, c_conj)
    return np.concatenate((ac - d_conjb, da + bc_conj))


def multiply_complex(i1, i2):
    # Complex multiplication (a,b)(c,d) = (ac - db,  ad + cb) where a,b,c,d are real numbers.
    # Note the lack of conjugates, as the conjugate of a real number is itself.
    if (i1.shape != (2,)) or (i2.shape != (2,)):
        raise ValueError("Imaginaries must have 2 components.")
    a = i1[0]
    b = i1[1]
    c = i2[0]
    d = i2[1]
    ac = a * c
    db = d * b
    ad = a * d
    cb = c * b
    return np.array([ac - db, ad + cb])



