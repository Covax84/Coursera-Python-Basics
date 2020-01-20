x = int(input())
mostMax = x
secondMax = 0
while x != 0:
    x = int(input())
    if x == 0:
        continue
    if x >= mostMax:
        secondMax = mostMax
        mostMax = x
    else:
        secondMax = x if x > secondMax else secondMax
print(secondMax)
