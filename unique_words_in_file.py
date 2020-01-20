file = open('input_unique.txt', 'r', encoding='utf8')
unique = set()
for i in file.read().split():
    unique.add(i)

print(len(unique))
file.close()
