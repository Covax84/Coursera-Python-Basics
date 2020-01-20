def power2(a: float, n: int):
    """
    Быстрое возведение в степень.
    при чётном n: а*а в степени n/2
    при нечётном n: a*(a**n-1)
    """
    if n == 0:
        return 1
    return a * power2(a, n - 1) if n % 2 != 0 else power2(a * a, n // 2)
# исправлено: убран elif n == 2: return a*a. n / 2 заменено n // 2 ^^


print(power2.__doc__[5:34])
x = float(input('Число: '))
y = int(input('Степень: '))
print('Ответ: ', end='')
print(power2(x, y))
