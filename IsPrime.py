def is_prime(n: int):
    """ is number prime. O(n**0.5) """
    divisor = 2
    while divisor <= n ** 0.5:
        if n % divisor == 0:
            return 'NO' if n != 2 else 'YES'
        divisor += 1
    return 'YES'


a = int(input())
print(is_prime(a))
