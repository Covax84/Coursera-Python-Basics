# Программа получает на вход в одной строке число S - размер диска (натуральное < 10000),
# и число N – количество пользователей (натуральное < 100),
# после этого идет N чисел(каждое в отдельной строке) - объем данных конкретного пользователя (натуральное < 1000)
# Вывести максимальное количество пользователей, чьи данные поместятся на диск.
m = list(map(int, input().split()))
users = []
amount = m[1]
while m[1] > 0:
    n = int(input())
    users.append(n)
    m[1] -= 1

while m[0] > 0 and len(users) > 0:
    m[0] -= min(users)
    if m[0] > 0:
        users.pop(users.index(min(users)))
    elif m[0] < 0:
        print(amount - len(users))
        break
    elif m[0] == 0:
        users.pop(users.index(min(users)))
        print(amount - len(users))
        break
else:
    print(amount - len(users))
