file = open('input_elections.txt', 'r', encoding='utf8')
dictionary = {}
counter = 0
for i in file.readlines():
    counter += 1
    dictionary[i.strip()] = dictionary.get(i.strip(), 0) + 1
dict_list = (sorted(dictionary, key=lambda x: dictionary[x], reverse=True))
file.close()
output = open('output_elections.txt', 'w', encoding='utf8')
if dictionary[dict_list[0]] > counter / 2:
    print(dict_list[0], file=output)
else:
    print(dict_list[0], dict_list[1], sep='\n', file=output)
output.close()
