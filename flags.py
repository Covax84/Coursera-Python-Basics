n = int(input())
top = '+___ '
num = '|{} / '
bot = '|__\\ '
stk = '|    '
print(top * n)
for i in range(1, n + 1):
    print(num.format(i), end='')
print()
print(bot * n)
print(stk * n)
