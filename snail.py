# улитка ползет по шесту высоты h, поднимаясь на a в день, сползая на b за ночь.
# на какой день улитка достигнет вершины шеста?
h = int(input())
a = int(input())
b = int(input())
print((h + a - 2 * b - 1) // (a - b))   # округление целочисленного деления вверх.
