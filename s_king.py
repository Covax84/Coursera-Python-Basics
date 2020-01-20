# ход короля.
# может ли король с клетки x,y попасть на клетку X,Y за 1 ход?
x = int(input())
y = int(input())
a = int(input())
b = int(input())
if x + 1 == a or x - 1 == a or x == a:
    if y + 1 == b or y - 1 == b or y == b:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
