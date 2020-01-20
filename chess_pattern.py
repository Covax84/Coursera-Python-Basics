a = int(input())
b = int(input())
c = int(input())
d = int(input())
sumAB = (a % 2 + b % 2) % 2
sumCD = (c % 2 + d % 2) % 2
if sumAB == sumCD:
    print('YES')
else:
    print('NO')
