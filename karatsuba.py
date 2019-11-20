import math

# multiplication huge values
class Karatsuba(object):
    @staticmethod
    def uncompose(a):
        if 2 <= len(a) <= 3:
            return a[:1], a[1:], 1
        if len(a) == 3:
            return a[:2], a[2:], 2
        half = int((math.floor(len(a) / 2)))
        x1 = a[:half]
        x0 = a[half:]
        return x1, x0, int(half)
    
    def karatsuba(self, a, b):
        x1, x0, m1 = Karatsuba.uncompose(a)
        y1, y0, m2 = Karatsuba.uncompose(b)
        z2 = int(x1) * int(y1)
        z1 = int(x1) * int(y0) + int(x0) * int(y1)
        z0 = int(x0) * int(y0)
        return z2 * int(math.pow(10, 2 * m1)) + z1 * int(math.pow(10, 1 * m1)) + z0
    

a = '123456'
b = '111111'
mult = Karatsuba()
print(mult.karatsuba(a, b))
print(int(a) * int(b))

        
