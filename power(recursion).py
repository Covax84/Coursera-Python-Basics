# возведение в степень рекурсией
def power(a, n):
    """ exponent n(int >= 0) of a(float) """
    if n == 0:
        return 1
    return power(a, n - 1) * a


x = float(input('Enter number: '))
y = int(input('Enter exponent: '))
print(power(x, y) if power(x, y) % 1 != 0 else int(power(x, y)))
