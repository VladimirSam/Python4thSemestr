import math
def f14(n):
    if n == 0:
        return 5
    else:
        return (math.tan(f14(n - 1))) + (1 / 67) *  f14( n - 1)**2
