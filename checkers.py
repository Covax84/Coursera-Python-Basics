# на курсере перепутаны вертикаль и горизонталь.
B, A = int(input()), int(input())  # первая клетка
Y, X = int(input()), int(input())  # вторая клетка
if (A + B) % 2 == (X + Y) % 2:
    if X - A > 0:
        if 0 > Y - B >= -(X - A):  # Y - B < 0 and Y - B >= -(X - a)
            print('YES')
        elif 0 <= Y - B <= X - A:  # Y - B >= 0 and Y - B <= X - a
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
