# вдоль дороги расположены селения и бомбоубежища
# определить для каждого селения ближайшее бомбоубежище
# ответ = список: индекс i - номер селения, значение i - номер убежища (начиная с 1)
towns = int(input())                            # количество селений
towns_pos = list(map(int, input().split()))     # расстояние от начала дороги до i-того селения
vaults = int(input())                           # количество бомбоубежищ
vaults_pos = list(map(int, input().split()))    # расстояние от начала дороги до i-того бомбоубежища

towns_tuple = []
vaults_tuple = []
for x in range(towns):
    towns_tuple.append((towns_pos[x], x))
for x in range(vaults):
    vaults_tuple.append((vaults_pos[x], x + 1))
ts = sorted(towns_tuple)
vs = sorted(vaults_tuple)
arr = [0] * towns
i = k = 0
while i < towns:
    if k + 1 >= vaults:
        arr[ts[i][1]] = vs[k][1]
        i += 1
    elif abs(ts[i][0] - vs[k + 1][0]) >= abs(ts[i][0] - vs[k][0]):
        arr[ts[i][1]] = vs[k][1]
        i += 1
    else:
        if k + 1 < vaults - 1:
            k += 1
        else:
            arr[ts[i][1]] = vs[k+1][1]
            i += 1
print(*arr)

# потестить:
# towns = 10
# towns_pos = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]     # расстояние от начала дороги до i-того селения
# vaults = 10
# vaults_pos = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]   # расстояние от начала дороги до i-того бомбоубежища
