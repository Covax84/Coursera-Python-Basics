# наименьший положительный элемент массива (элементы <= 1000)
n = list(map(int, input().split()))
counter = 1000
for i in range(len(n)):
    if 0 < n[i] <= counter:
        counter = n[i]
print(counter)

a = [1, 2, 3, 4, 5, 6, 7, 8]
a.remove()
