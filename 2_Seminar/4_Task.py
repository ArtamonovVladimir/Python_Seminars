# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, в порядке невозрастания.
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию,
# если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего).
# Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите рост Пети: '))
            if input_number <= 0:
                print('Попробуйте ввести еще раз и число больше 0')
                continue
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


petya_height = input_data_check()
students_height = [165, 163, 160, 160, 157, 157, 155, 154]
if petya_height > students_height[0]:
    print('У Пети 1 место')
elif petya_height <= students_height[-1]:
    print(f'У Пети {len(students_height) + 1} место')
else:
    for i in range(len(students_height)):
        if students_height[i] >= petya_height and students_height[i+1] < petya_height:
            print(f'У Пети {i+2} место')
            break
