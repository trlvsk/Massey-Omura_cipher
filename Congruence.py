from functools import reduce
from Prime import gcd
"""
def extendedEuclideanAlgorithm(a, b):
    
        Calculates gcd(a,b) and a linear combination such that
        gcd(a,b) = a*x + b*y

        As a side effect:
        If gcd(a,b) = 1 = a*x + b*y
        Then x is multiplicative inverse of a modulo b.
    
    aO, bO = a, b

    x = lasty = 0
    y = lastx = 1
    while b != 0:
        q = a / b
        a, b = b, a % b
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return {"x": lastx, "y": lasty, "gcd": aO * lastx + bO * lasty}

def congruence(rests, modulos):
    assert len(rests) == len(modulos)
    x = 0
    M = reduce(lambda x, y: x * y, modulos)

    for mi, resti in zip(modulos, rests):
        Mi = M / mi
        s = extendedEuclideanAlgorithm(Mi, mi)["x"]
        e = s * Mi
        x += resti * e
    return {"congruence class": ((x % M) + M) % M, "modulo": M}
"""
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = iterative_egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

