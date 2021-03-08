import math

def f13(n):
    sum1 = 0
    sum2 = 0
    for i in range (1, n+1):
        sum1 += (abs(math.sin(i) + i**4 + 27) + 13 * i**4)
    for i in range (1, n+1):
        sum2 += (i**5 - math.exp(i))
    return sum1 + sum2 * 49
res1 = f13(55)
res2 = f13(13)
print ('%.2e' % res1)
print ('%.2e' % res2)