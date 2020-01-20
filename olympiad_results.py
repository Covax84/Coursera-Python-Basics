# Программа получает на вход число участников олимпиады N.
# Далее идет N строк, в каждой строке записана фамилия участника,
# затем, через пробел, набранное им количество баллов.
#
# Выведите список участников (только фамилии) в порядке убывания набранных баллов.

n = int(input())
members = []
for i in range(n):
    members.append(input().split())

members = list(map(lambda x: (x[0], int(x[1])), members))

members.sort(key=lambda x: x[-1], reverse=True)
for i in members:
    print(i[0])
