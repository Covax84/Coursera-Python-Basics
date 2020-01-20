# какое наибольшее число подряд идущих элементов этой последовательности равны друг другу
x = int(input())
longestSeq = 1 if x else 0
candidate = 1 if x else 0
tmp = x if x else 0
while x != 0:
    x = int(input())
    if x == tmp:
        candidate += 1
        tmp = x
    elif x != tmp:
        longestSeq = candidate if longestSeq < candidate else longestSeq
        tmp = x
        candidate = 1
print(longestSeq)
