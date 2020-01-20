file = open('input_count.txt', 'r', encoding='utf8')
dictionary = {}
for i in file.read().split():
    print(dictionary.get(i, 0), end=' ')
    dictionary[i] = dictionary.get(i, 0) + 1
print()