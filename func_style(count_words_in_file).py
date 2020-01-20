# Посчитать количество уникальных слов в файле, функциональный стиль курсеры.
print(
    len(
        set(
            open('input_func.txt', 'r', encoding='utf8').read().split()
        )
    )
)
