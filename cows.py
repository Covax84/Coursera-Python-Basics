n = int(input())
if 10 < n < 20:
    print(str(n) + ' коров')
elif n % 10 == 1:
    print(str(n) + ' корова')
elif 5 > n % 10 > 1:
    print(str(n) + ' коровы')
else:
    print(str(n) + ' коров')
