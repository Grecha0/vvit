print('Решаем уравнение a*x²+b*x+c=0')
a = input('Введите значение a: ')
b = input('Введите значение b: ')
c = input('Введите значение c: ')
a = float(a)
b = float(b)
c = float(c)
d = b**2 - 4*a*c
print('Дискриминант = ' + str(d))
if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / (2 * a)
    print('x = ',x)
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x1 = ',x1)
    print('x2 = ',x2)