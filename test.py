print('Введите коэффициенты a, b и с для решения квадратного уравнения: a*x^2+b*x+c=0')

a = float(input('Введите а ='))
while a == 0:
    print('Введите число не равное 0 для a')
    a = float(input('Введите а ='))

b = float(input('Введите b ='))
c = float(input('Введите c ='))
d = b ** 2 - 4 * a * c

import math
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('x1 =', x1, 'x2 =', x2)
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print('x =', x)
else:
    print('Нет действительных корней.')

