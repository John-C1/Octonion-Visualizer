"""
Unit tests on octonion algebraic operations.
"""

from octonions.algebra import Octonion
import numpy as np

octonion1 = Octonion([0,0,0,0,0,0,0,1])
octonion2 = Octonion([0,0,0,0,0,0,1,0])
octonion3 = Octonion([3.1,2.5,-7.9,0.4,1.2,-3.3,0.0,5.6])
x1 = Octonion([0,1,0,0,0,0,0,0])
x2 = Octonion([0,0,1,0,0,0,0,0])
x3 = Octonion([0,0,0,1,0,0,0,0])

def test_addition():
    result = octonion1 + octonion2
    expected = Octonion([0,0,0,0,0,0,1,1])
    assert result == expected

def test_subtraction():
    result = octonion3 - octonion2
    expected = Octonion([3.1,2.5,-7.9,0.4,1.2,-3.3,-1.0,5.6])
    assert result == expected

def test_conjugation():
    result = octonion3.conjugate()
    expected = Octonion([3.1,-2.5,7.9,-0.4,-1.2,3.3,0.0,-5.6])
    assert result == expected

def test_norm():
    result1 = octonion3.norm()
    expected1 = np.sqrt(3.1**2 + 2.5**2 + (-7.9)**2 + 0.4**2 + 1.2**2 + (-3.3)**2 + 0.0**2 + 5.6**2)
    assert np.isclose(result1, expected1)
    result2 = octonion1.norm()
    assert result2 == 1.0

def test_equal():
    octonion4 = Octonion([3.1,2.5,-7.9,0.4,1.2,-3.3,0.0,5.6])
    assert octonion3 == octonion4

def test_multiplication_noncommutativity():
    x1_negative = Octonion([0,-1,0,0,0,0,0,0])
    x2_negative = Octonion([0,0,-1,0,0,0,0,0])
    x3_negative = Octonion([0,0,0,-1,0,0,0,0])
    assert x1 * x2 == x3
    assert x3 * x1 == x2    
    assert x2 * x3 == x1
    assert x2 * x1 == x3_negative
    assert x1 * x3 == x2_negative
    assert x3 * x2 == x1_negative

def test_multiplication_nonassociativity():
    assert (x1*x2)*x3 == Octonion([-1,0,0,0,0,0,0,0])
    assert x1*(x2*x3) == Octonion([-1,0,0,0,0,0,0,0])
    o_nonassociative = Octonion([0,1,0,5,0,0,0,4])
    print (o_nonassociative*(x1*x2))
    print ((o_nonassociative*x1)*x2)
    assert (o_nonassociative*x1)*x2 == Octonion([-5,0,-1,0,-4,0,0,0])
    assert o_nonassociative*(x1*x2) == Octonion([-5,0,-1,0,4,0,0,0])
    
    
