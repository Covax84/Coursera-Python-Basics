# сортировка значений трёх чисел, методом кортежного присваивания.
A, B, C = int(input()), int(input()), int(input())
if A >= B:
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
print(A, B, C)
