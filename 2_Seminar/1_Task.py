# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

import random

coins_quantity = int(input('Введите количество монеток: '))
coins = []
sum = 0
for i in range(coins_quantity):
    coins.append(random.randint(0, 1))
    sum += coins[i]
print(coins)
if sum == coins_quantity or sum == 0:
    print('Переворачивать монетки не нужно, все на одной стороне')
elif sum > (coins_quantity // 2):
    print(f'Нужно перевернуть {coins_quantity - sum}')
else:
    print(f'Нужно перевернуть {sum}')
