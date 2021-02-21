import math

def f12(x):
    if x < 97:
        return (96 * x**5 - 80 * x**3 - 73)**7 - 64 * x**3
    elif 97 <= x < 108:
        return math.exp( math.sin(x**2)) - 94 * x
    elif 108 <= x < 158:
        return ( math.exp(x) - x / 33 - 64)**2 - 60 * x**3
    else:
        return 11 * (x**6 + 58 * x**4)**6 + 24 * x**5
res1 = f12(183)
res2 = f12(169)
print ('%.2e' % res1)
print ('%.2e' % res2)
