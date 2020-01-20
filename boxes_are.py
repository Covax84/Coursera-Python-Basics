A, B, C = int(input()), int(input()), int(input())  # первая коробка
X, Y, Z = int(input()), int(input()), int(input())  # вторая коробка
if A >= B:                                          # кортежная сортировка по сторонам a<B<C
    A, B = B, A
    if B >= C:
        B, C = C, B
        if A >= B:
            A, B = B, A
elif A <= B:
    if B >= C:
        B, C = C, B
        if A >= B:
            A, B = B, A
if X >= Y:                                           # кортежная сортировка по сторонам X<Y<Z
    X, Y = Y, X
    if Y >= Z:
        Y, Z = Z, Y
        if X >= Y:
            X, Y = Y, X
elif X <= Y:
    if Y >= Z:
        Y, Z = Z, Y
        if X >= Y:
            X, Y = Y, X
if A == X and B == Y and C == Z:
    print('Boxes are equal')
elif A <= X and B <= Y and C <= Z:
    print('The first box is smaller than the second one')
elif A >= X and B >= Y and C >= Z:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
