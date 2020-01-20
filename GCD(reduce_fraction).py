def gcd(a, b):
    """ алгоритм Евклида для 2-х целых положительных чисел """
    if a % b != 0:
        return gcd(b, a % b)
    return b


def reduce_fraction(n, m):
    """ сокращение дроби n/m алгоритмом Евклида """
    return n // gcd(n, m), m // gcd(n, m)


x = int(input())
y = int(input())
print(*reduce_fraction(x, y))
