# система линейных уравнений - 1
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
# ax + by = e
# cx + dy = f
if (d * a - b * c) != 0:
    x = (d * e - f * b) / (d * a - b * c)
    y = (f * a - e * c) / (d * a - b * c)
else:
    x = (d * e - f * b)
    y = (f * a - e * c)
print(x, y)
