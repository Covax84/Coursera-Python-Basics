# при помощи reduce вывести произведение пятых степеней последовательности
# 3й параметр в reduce - стартовый
from functools import reduce
print(
    reduce(
        lambda x, y: x * y**5,
        map(
            int,
            open('input_reduce.txt', 'r', encoding='utf8').read().split()),
        1)
)
