def distance(a, b, c, d):
    """ по координатам точек определяет расстояние между ними на плоскости """
    cathetus1 = abs(a) - abs(c) if a * c > 0 else abs(a) + abs(c)
    cathetus2 = abs(b) - abs(d) if b * d > 0 else abs(b) + abs(d)
    return (cathetus1**2 + cathetus2**2) ** 0.5  # корень из суммы квадратов катетов = гипотенуза


# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# print(distance(a, b, c, d))
