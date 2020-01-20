x = float(input())
y = float(input())


def is_point_in_square(a, b):
    return -1 <= a <= 1 and -1 <= b <= 1


print('YES' if is_point_in_square(x, y) else 'NO')
