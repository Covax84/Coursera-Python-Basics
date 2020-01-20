m = int(input())
n = int(input())
k = int(input())
if k <= n * m:
    if (n * m - k) % n == 0 or (n * m - k) % m == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
