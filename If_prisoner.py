# Узник замка Иф.
# Можно ли выбросить в отверстие размером D x E кирпичи размером a x B x C ?
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A <= D:
    if B <= E or C <= E:
        print('YES')
    else:
        print('NO')
elif B <= D:
    if C <= E or A <= E:
        print('YES')
    else:
        print('NO')
elif C <= D:
    if A <= E or B <= E:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
