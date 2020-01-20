x = int(input())
seqSum = 0 if x == 0 else x
counter = 1
while x != 0:
    x = int(input())
    seqSum += x
    if x == 0:
        continue
    counter += 1
print(seqSum/counter)
