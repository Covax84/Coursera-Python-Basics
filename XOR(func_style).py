# XOR для двух последовательностей состоящих из 0 и 1, функциональный стиль курсеры, что.
print(
    *map(
        lambda x: int(x[0] != x[1]),
        (zip(
            map(
                int,
                input().split()),
            map(
                int,
                input().split())
        )
        )
    )
)
