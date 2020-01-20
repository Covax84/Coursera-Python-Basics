# задание coursera. поиск минимального делителя за O(n**0.5)
def min_divisor(n: int):
    """ returns minimal divisor of n """
    divisor = 2
    while divisor <= n ** 0.5:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n if n % 2 != 0 else 2


a = int(input('Введите число, для поиска минимального делителя: '))
print(min_divisor(a))
