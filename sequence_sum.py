def SequenceSum(n):
    """ сумма вводимой последовательности, заканчивающаяся нулём """
    x = int(input()) if n != 0 else 0
    if x != 0:
        return SequenceSum(n + x)
    return n


m = int(input())
print(SequenceSum(m))
