# количество элементов последовательности, равных максимуму
x = int(input())
maxNum = x if x != 0 else 0
counter = 1 if x != 0 else 0
while x != 0:
    x = int(input())
    if x > maxNum:
        maxNum = x
        counter = 1
    elif x == maxNum:
        counter += 1
print(counter)
