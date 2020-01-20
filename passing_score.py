def solution(n, arr):
    if len(arr) <= n:
        return 0
    elif arr[0] == arr[n]:
        return 1
    for i in range(n, 0, -1):
        if arr[i] < arr[i - 1]:
            return arr[i - 1]


input_file = open('input_ball.txt', 'r', encoding='utf8')
k = int(input_file.readline())
total_points = []
for line in input_file:
    a, b, c = (map(int, line.split()[-3:]))
    if a >= 40 and b >= 40 and c >= 40:
        total_points.append(a + b + c)
input_file.close()
total_points.sort(reverse=True)
output_file = open('output.txt', 'w', encoding='utf8')
print(solution(k, total_points), file=output_file)
output_file.close()
