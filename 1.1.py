import math
def f11(x, y):
    return abs((math.sin(x) + y**4 + 27) + 13 * x**3) / (y**3 - y**6 - 56) + math.sqrt(y**6 - (y**7/82)) + ((y**7 - math.exp(y)) / (11 * y**6 + x**5))
res1 = f11(2, -45)
res2 = f11(-69, 54)
print ('%.2e' % res1)
print ('%.2e' % res2)