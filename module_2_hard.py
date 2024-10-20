from random import randint

stone_1 = int(randint(3, 20))
ilya_1 = []
print(f'Число на первом камне: {stone_1}')
for i in range(1, stone_1):
    for j in range(1, stone_1):
        if i != j:
            if stone_1 % (i + j) == 0:
                if i and j in ilya_1:
                    continue
                else:
                    ilya_1.extend([i, j])
print("Код для второго камня:", *ilya_1)
