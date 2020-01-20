n = list(map(int, input().split()))


def CountSort(A):
    freq = [0] * 101
    string = ''
    for number in A:
        freq[number] += 1

    for i in range(len(freq)):
        string += (str(i) + ' ') * freq[i]

    sorted_n = string.split()

    for i in range(len(A)):
        A[i] = int(sorted_n[i])


CountSort(n)
print(*n)
