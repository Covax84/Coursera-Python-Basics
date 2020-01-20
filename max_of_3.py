# a = int(input())
# Y = int(input())
# Z = int(input())
# if Y <= a >= Z:
#     print(a)
# elif a <= Y >= Z:
#     print(Y)
# else:
#     print(Z)


def max_of_3(a, b, c):
    if b <= a >= c:
        return a
    elif a <= b >= c:
        return b
    else:
        return c


def test_1(func):
    print('test_1: ', end='')
    A, B, C = 1, 2, 3
    print('success' if func(A, B, C) == 3 else 'Failed')


def test_2(func):
    print('test_2: ', end='')
    A, B, C = 2, 2, 3
    print('success' if func(A, B, C) == 3 else 'Failed')


def test_3(func):
    print('test_3: ', end='')
    A, B, C = 1, 3, 2
    print('success' if func(A, B, C) == 3 else 'Failed')


def test_4(func):
    print('test_4: ', end='')
    A, B, C = 3, 2, 1
    print('success' if func(A, B, C) == 3 else 'Failed')


def test_5(func):
    print('test_5: ', end='')
    A, B, C = 1, 2, 1
    print('success' if func(A, B, C) == 2 else 'Failed')


def test_6(func):
    print('test_6: ', end='')
    A, B, C = 1, 2, 0
    print('success' if func(A, B, C) == 2 else 'Failed')


def test_7(func):
    print('test_7: ', end='')
    A, B, C = 0, 2, 0
    print('success' if func(A, B, C) == 2 else 'Failed')


def test_8(func):
    print('test_8: ', end='')
    A, B, C = 1, 1, 0
    print('success' if func(A, B, C) == 1 else 'Failed')


def test_9(func):
    print('test_9: ', end='')
    A, B, C = 0, 0, 1
    print('success' if func(A, B, C) == 1 else 'Failed')


def test_10(func):
    print('test_10: ', end='')
    A, B, C = 2, 1, 5
    print('success' if func(A, B, C) == 5 else 'Failed')


test_1(max_of_3)
test_2(max_of_3)
test_3(max_of_3)
test_4(max_of_3)
test_5(max_of_3)
test_6(max_of_3)
test_7(max_of_3)
test_8(max_of_3)
test_9(max_of_3)
test_10(max_of_3)
