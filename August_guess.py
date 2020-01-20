# Первая строка входных данных содержит число n — наибольшее число,
# которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO. Наконец,
# последняя строка входных данных содержит одно слово HELP.
# Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.
k = int(input())
guess_set = set(range(1, k + 1))
while True:
    Beatrice = input().split()
    if Beatrice[0] == 'HELP':
        break
    Beatrice = set(map(int, Beatrice))
    August = input()
    if August == 'YES':
        guess_set.intersection_update(Beatrice)  # пересечение guess_set и Beatrice
    elif August == 'NO':
        guess_set.difference_update(Beatrice)    # входит в guess_set, но не входят в Beatrice
print(*sorted(list(guess_set)))
