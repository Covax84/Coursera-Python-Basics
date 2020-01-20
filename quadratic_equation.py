# квадратное уравнение: ax² + bx + c
# дискриминант: D = b² - 4ac
# вывести корни в порядке возрастания
a = float(input())
b = float(input())
c = float(input())
d = b**2 - (4 * a * c)
if d > 0:
    x = (-b - d ** 0.5) / (2 * a)
    y = (-b + d ** 0.5) / (2 * a)
    if x < y:
        print(x, y)
    else:
        print(y, x)
elif d == 0:
    print(-(b / (2 * a)))
