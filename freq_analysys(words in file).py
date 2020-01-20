# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
#
# Указание.
# После того, как вы создадите словарь всех слов, вам захочется отсортировать его
# по частоте встречаемости слова. Желаемого можно добиться, если создать список,
# элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
# Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет
# сортировать список кортежей, при этом кортежи сравниваются по первому элементу,
# а если они равны —то по второму. Это почти то, что требуется в задаче.
file = open('input_freq.txt', 'r', encoding='utf8')
dictionary = {}
arr = []
for i in file.read().split():
    dictionary[i] = dictionary.get(i, 0) + 1
for k in dictionary:
    tmp = dictionary[k], k
    arr.append(tmp)
arr.sort(key=lambda x: (-int(x[0]), x[1]))  # хитрый сорт, по одному значению вверх, по второму вниз!
for i in range(len(arr)):
    print(arr[i][1])
# INPUT:
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
#
# OUTPUT:
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your
