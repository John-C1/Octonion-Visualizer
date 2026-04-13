"""
Implements Rehm's Algorithm for factoring octonions.
"""

import math
import random

import algebra
import cayley_integers as ci

def factor_octonion(oct):
    """
    Implementation of Rehm's Algorithm for factoring primitive octavian integers.
    """
    # Can't factor with norm of 0.
    if oct.norm() == 0:
        return [algebra.Octonion(0)]
    
    if not check_primitive(oct):
        print("Rehm's Algorithm does no apply to non-primitive octavians.")
        return [algebra.Octonion(0)]
    
    # Use the squared norm
    norm = round(oct.norm() ** 2)
    # Pick m s.t. m < sqrt(norm) and m > 1. Smallest prime factor is simplest
    m = smallest_prime_factor(norm)
    if m is None:
        # Norm is prime, so oct is irreducible nontrivially.
        print("Norm is prime, so oct is irreducible nontrivially.")
        return [oct]
    
    quotients, p_values, m_values = forward_pass(oct, m)
    leftHand, rightHand = reverse_pass(oct, quotients, p_values, m_values)
    return leftHand, rightHand
    

def forward_pass(p, m):
    """
    Strategy:
    Performs the forward pass of Rehm's algorithm, which returns a set of 
    quotients and p values that are then fed through the reverse pass to 
    generate 2 sets of 240 divisors. 
    """
    quotients = []
    p_values = []
    m_values = []
    while m != 0:
        # Divide all components of p by m.
        q = algebra.Octonion([x / m for x in p.components])
        q = nearest_octavian_integer(q)
        quotients.append(q)
        p_values.append(p)
        m_values.append(m)
        print(m)
        # Find remainder and conugate it.
        r = p - algebra.Octonion([x * m for x in q.components])
        r_conj = r.conjugate()
        # Compute new p and m values.
        p = r_conj
        m = int(round((p.norm() ** 2 / m)))

    return quotients, p_values, m_values

def reverse_pass(oct, quotients, p_values, m_values):
    leftHand = []
    rightHand = []
    m_N = m_values[-1]

    for k in range(1, 241):
        u_n = ci.oct_int(m_N, k)
        if u_n is None:
            continue

        current = quotients[-1] * u_n
        previous = u_n

        verify_index = -2
        for quotient in reversed(quotients[:-1]):
            new_current = quotient * current + previous
            previous = current
            current = new_current

            expected_m = m_values[verify_index]
            actual_m = round(current.norm() ** 2)
            if actual_m != expected_m:
                print(f"Warning: norm mismatch at step {verify_index}. Expected {expected_m}, got {actual_m}")
            verify_index -= 1

        leftHand.append(current)
        rightHand.append(previous.conjugate())



    return leftHand, rightHand


def smallest_prime_factor(n):
    if n <= 1:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return None # Norm is already prime.


def check_primitive(oct):
    """
    Checks to see if the octavian integer is primitive.
    This occurs when gcd of all components is 1.
    """
    from math import gcd
    from functools import reduce
    # Double so 1/2 components become integers and gcd can be applied.
    doubled = [round(x * 2) for x in oct.components]
    # Finds highest common divisor. 
    # Cayley integer has either all 1/2 components or all integer components, so <= 2 counts doubling.
    return reduce(gcd, doubled) <= 2


def generate_primitive_octonion(n):
    """
    Generates a primitive integral octonion with norm n.
    """
    for k in range(1, 241):
        oct = ci.oct_int(n, k)
        if oct is not None and check_primitive(oct):
            return oct
    return None
    

def nearest_octavian_integer(oct):
    """
    For any point x in R^8, there exists a Cayley Integer y such that 
    squared norm(x-y) <= 1/2.) This function finds Cayley Integer y.
    Due to the property in Rehm's algortihm that such an octavian must exist,
    we can simply round to the closest "possible" e8 lattice points and one must work.
    """
    # Transform the octonion to the e8 space
    e8_oct = oct_to_e8(oct)
    # Convert the tuple to an "octonion" for easier manipulation.
    e8_oct = algebra.Octonion(e8_oct)
    # Round every component to nearest integer
    cand_a = algebra.Octonion([math.floor(x + 0.5) for x in e8_oct.components])
    # Find the index of the component closest to a half integer and store it.
    cand_a_swap = max(range(8), key=lambda i: abs(e8_oct.components[i] - math.floor(e8_oct.components[i] + 0.5)))
    # Round every component to nearest half-integer
    cand_b = algebra.Octonion([math.floor(x) + 0.5 for x in e8_oct.components])
    # For cand_b, find component closest to a whole integer and store it.
    cand_b_swap = max(range(8), key=lambda i: abs(e8_oct.components[i] - math.floor(e8_oct.components[i] + 0.5)))

    s1 = sum(math.floor(x + 0.5) for x in cand_a.components)
    s2 = sum(math.floor(x) for x in cand_b.components)
    if (s1 % 2 != 0):
        # cand_a is not in the e8 lattice, so make the swap that makes smallest difference to norm.
        cand_a.components[cand_a_swap] += 1 if e8_oct.components[cand_a_swap] > cand_a.components[cand_a_swap] else -1
    if (s2 % 2 != 0):
        cand_b.components[cand_b_swap] += 1 if e8_oct.components[cand_b_swap] > cand_b.components[cand_b_swap] else -1

    # Convert back to a tuple and then convert to octonions.
    cand_a_tup = cand_a.components
    cand_b_tup = cand_b.components
    cand_a = ci.e8_to_oct(cand_a_tup)
    cand_b = ci.e8_to_oct(cand_b_tup)

    # Return whichever is closer to oct.
    if (oct - cand_a).norm() <= (oct - cand_b).norm():
        return cand_a
    else:
        return cand_b

def oct_to_e8(oct):
    """
    Performs the inverse transformation of the e8_to_oct function in cayley_integers.py, 
    which transforms an octonion to the e8 lattice space.
    Returns a tuple of 8 e8 lattice components.
    """
    tup = [0] * 8
    tup[0] = oct.components[0] + oct.components[1]
    tup[1] = oct.components[1] - oct.components[0]
    tup[2] = oct.components[2] + oct.components[3]
    tup[3] = oct.components[2] - oct.components[3]
    tup[4] = oct.components[4] + oct.components[5]
    tup[5] = oct.components[4] - oct.components[5]
    tup[6] = oct.components[6] + oct.components[7]
    tup[7] = oct.components[6] - oct.components[7]
    return tup


    
if __name__ == "__main__":
    p = generate_primitive_octonion(6)
    print("Input:", p)
    left, right = factor_octonion(p)
    print(f"Got {len(left)} left divisors and {len(right)} right divisors")
    # Verify first pair: left[0] * right[0] should equal p
    product = left[0] * right[0]
    print("left[0] * right[0] == p:", (product - p).norm() < 0.01)

