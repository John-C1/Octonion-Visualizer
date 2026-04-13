from math import isqrt
import random
from algebra import Octonion

def ball_search(k, remaining, prefix=()):
    if k == 0:
        yield prefix
        return

    lo = isqrt(remaining)
    for i in range(-lo, lo + 1): 
        yield from ball_search(k - 1, remaining - i*i, prefix + (i,))

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
    vec = e8_lattice_vector(p,k)
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