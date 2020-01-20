def SequenceReverse(n):
    """ разворот вводимой последовательности, заканчивающейся нулём """
    if n != 0:
        n = int(input())
        SequenceReverse(n)
        print(n)
    return m


m = int(input())
print(SequenceReverse(m))
