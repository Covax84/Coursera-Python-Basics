# сортировка значений трёх чисел, методом кортежного присваивания.
a, b, c = map(int, input().split())


# def sort_abc(a, b, c):
#     """ """
#     if a >= b:
#         a, b = b, a
#         if b >= c:
#             b, c = c, b
#             if a >= b:
#                 a, b = b, a
#     elif a <= b:
#         if b >= c:
#             b, c = c, b
#             if a >= b:
#                 a, b = b, a
#     return a, b, c


def sort_abc_simply(a, b, c):
    """ упрощенная версия сортировки 3-х чисел(кортежное присваивание) """
    if a > b:
        a, b = b, a

    if b > c:
        b, c = c, b

    if a > b:
        a, b = b, a

    return a, b, c


print(sort_abc_simply(a, b, c))
