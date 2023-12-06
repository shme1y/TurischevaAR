import math
def med(a, b, c):
 return math.sqrt(2*a+2*b - c) / 2
a = int(input('Введите сторону A: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))
z = med(a, b, c)
print(med(z, z, z))