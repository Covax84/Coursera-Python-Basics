# найти максимум и индекс его последнего вхождения
n = list(map(int, input().split()))
counter = 0, 0
for i in range(len(n)):
    if n[i] >= counter[0]:
        counter = n[i], i
print(*counter)
