from math import pi, acos, cos, sqrt
from fractions import gcd
mod = 7 + 10**9
mul = 10**20


def modulo_inverse(x):
    if x == 1:
        return 1
    return 1


for _ in xrange(input()):
    l, d, t = map(float, raw_input().split())

    x = acos(d/l) * t
    position = x/(2*pi)
    position -= int(position)
    position *= 2*pi
    sign = 1

    if position <= pi/2: pass
    elif position < pi:
        sign = -1
        position = pi - position
    elif position < 3*pi/2:
        sign = -1
        position -= pi
    else:
        position = 2*pi - position

    y = (cos(position) * l)*sign
    y *= mul
    y = int(y)
    div = gcd(y, mul)
    numerator = y/div
    denominator = mul/div
    # y %= mod
    # print y*mul, div, numerator, denominator, mul
    if int(sqrt(pow(l, 2)-pow(d, 2))) != (sqrt(pow(l, 2)-pow(d, 2))):
        raise ValueError
    print y  # (numerator * modulo_inverse(denominator)) % mod
