n = int(input())

for i in range(1, n+1):
    print(*[x for x in range(1, i+1)], sep='')

#  ИЛИ

for i in range(1, n+1):
    print(*range(1, i+1), sep='')
