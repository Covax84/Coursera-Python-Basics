n = int(input())
minimal_divisor = n
k = n
while k > 1:
    if n % k == 0:
        minimal_divisor = k
        k -= 1
    else:
        k -= 1
print(minimal_divisor)
