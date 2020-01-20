# принадлежит ли точка(x, y) кругу (радиус r, центр xc, yc)
def IsPointInCircle(x, y, xc, yc, r):
    return catX <= r >= catY and hipXY <= r


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if xc >= 0 <= x:
    catX = x - xc if x > xc else xc - x
elif xc <= 0 >= x:
    catX = abs(xc) - abs(x) if x > xc else abs(x) - abs(xc)
else:
    catX = abs(x) + abs(xc)

if yc >= 0 <= y:
    catY = y - yc if y > yc else yc - y
elif yc <= 0 >= y:
    catY = abs(yc) - abs(y) if y > yc else abs(y) - abs(yc)
else:
    catY = abs(y) + abs(yc)

hipXY = (catX ** 2 + catY ** 2) ** 0.5

if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')

# test6: ('NO')
# -7
# 15
# 14
# -3
# 27.658
#
# test7: ('YES')
# -7
# 15
# 14
# -3
# 27.659