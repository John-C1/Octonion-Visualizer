from math import isqrt
import random
from algebra import Octonion
from sympy.ntheory import divisor_sigma

def ball_search(k, remaining, prefix=()):
    if k == 0:
        yield prefix
        return

    lo = isqrt(remaining)
    for i in range(-lo, lo + 1): 
        yield from ball_search(k - 1, remaining - i*i, prefix + (i,))

def r_4(n):
    if n == 0:
        return 1
    elif n%4 == 0:
        return 8 * divisor_sigma(n) - 32 * divisor_sigma(round(n/4))
    else:
        return 8 * divisor_sigma(n)

def d4_integer(p,k):
    count = k
    for tup in ball_search(4, p):
        t = sum(i**2 for i in tup)
        if t == p:
            count = count - 1
            if count < 0:
                return list(tup)
    return None

def d4_half_integer(p,k):
    count = k
    for tup in ball_search(4, p + 1 + isqrt(4 * p)):
        t = sum(i**2 + i for i in tup)
        if t + 1 == p and tup[3] >= 0:
            count = count - 1
            if count < 0:
                return list(tup)
    return None

def e8_lattice_quick(p,k):
    count = k
    for i in range(2*p+1):
        r4_i = r_4(i)
        r4_j = r_4(2*p - i)
        # Either i even or odd, we have integer points
        deduct = r4_i * r4_j
        if count >= deduct:
            count = count - deduct
        else:
            k_1 = count // r4_j
            k_2 = count % r4_j
            return d4_integer(i, k_1) + d4_integer(2*p - i, k_2)
        # If i odd, additional half-integer points
        if i%2 == 1:
            if count >= 2 * deduct:
                count = count - 2 * deduct
            elif count < deduct:
                k_1 = count // r4_j
                k_2 = count % r4_j
                lst_new = d4_half_integer(i, k_1) + d4_half_integer(2*p - i, k_2)
                if sum(i for i in lst_new) % 2 == 1:
                    lst_new[7] = -1 - lst_new[7]
                return [i + 0.5 for i in lst_new]
            else:
                k_1 = (count - deduct) // r4_j
                k_2 = count % r4_j
                lst_new = d4_half_integer(i, k_1) + d4_half_integer(2*p - i, k_2)
                lst_new[3] = -1 - lst_new[3]
                if sum(i for i in lst_new) % 2 == 1:
                    lst_new[7] = -1 - lst_new[7]
                return [i + 0.5 for i in lst_new]
    return None

def e8_lattice_vector(p,k):
    count = k
    for tup in ball_search(8, 2*p + 2 + isqrt(16 * p)):
        s = sum(i for i in tup)
        t = sum(i**2 for i in tup)
        if s%2 == 0 and t == 2*p:
            count = count - 1
            if count == 0:
                return tup
        if s%2 == 0 and t+s+2 == 2*p:
            count = count - 1
            if count == 0:
                return tuple(i + 0.5 for i in tup)
    return None

def e8_to_oct(tup):
    return Octonion([
        (tup[0]-tup[1])/2, (tup[0]+tup[1])/2,
        (tup[2]+tup[3])/2, (tup[2]-tup[3])/2,
        (tup[4]+tup[5])/2, (tup[4]-tup[5])/2,
        (tup[6]+tup[7])/2, (tup[6]-tup[7])/2
    ])

def oct_int(p,k):
    # vec = e8_lattice_vector(p,k)
    vec = e8_lattice_quick(p,k)
    if vec is None:
        return None
    else:
        return e8_to_oct(vec)

def generate_240_unit_cayley_integers():
    cayley_integers = []
    for k in range(1, 241):
        oct = oct_int(1, k)
        if oct is not None:
            cayley_integers.append(oct)
    return cayley_integers

if __name__ == "__main__":
    p = 1
    k1 = random.randint(1, 240)
    print("a is the", k1, "-th unit Cayley Octonion")
    oct_a = oct_int(p,k1)
    k2 = random.randint(1, 240)
    print("b is the", k2, "-th unit Cayley Octonion")
    oct_b = oct_int(p,k2)
    oct_ab = oct_a * oct_b
    oct_ba = oct_b * oct_a
    for i in range(1, 241):
        oi = oct_int(p, i)
        if (oct_ab - oi).norm() < 0.01:
            print("ab is the", i, "-th unit Cayley Octonion")
        if (oct_ba - oi).norm() < 0.01:
            print("ba is the", i, "-th unit Cayley Octonion")
    unit_cayleys = generate_240_unit_cayley_integers()
    print("The 240 unit Cayley integers are:")
    for i, oct in enumerate(unit_cayleys):
        print(f"{i+1}: {oct}")
