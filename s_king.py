# ��� ������.
# ����� �� ������ � ������ x,y ������� �� ������ X,Y �� 1 ���?
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
