# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

mass = input('Введите через пробел числа: ').split()
gap = int(input('Введите число для сдвига: '))
new_mass = []
for i in range(len(mass)):
    if gap >= 0:
        step = i + gap - 1
        if step > len(mass)-1:
            step = i + gap - 1 - len(mass)
    if gap < 0:
        step = i + gap + 1
    new_mass.append(int(mass[step]))

print(new_mass)
