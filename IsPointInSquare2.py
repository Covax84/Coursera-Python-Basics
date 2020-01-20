# принадлежит ли точка ромбу (от 1 до -1 по x и по y)
a = float(input())
b = float(input())
e = 1e-06


def is_point_in_square2(x, y):
    return 1 - abs(y) + e >= abs(x) <= 1 and 1 - abs(x) + e >= abs(y) <= 1


print('YES' if is_point_in_square2(a, b) else 'NO')
