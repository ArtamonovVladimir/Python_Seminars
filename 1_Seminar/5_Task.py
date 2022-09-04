# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_data_check(col):
    text = ['x', 'y']
    xy_list = []
    k = 0
    for k in range(col):
        i = True
        while i:
            try:
                input_number = int(
                    input(f'Введите координату {text[k]}: '))
                i = False
                xy_list.append(input_number)
            except ValueError:
                print('Ввод данных не верен, повторите ввод!')

    return xy_list


def distance_calculation(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return distance


quantity = 2
print('Введите координаты точки A')
a_point = input_data_check(quantity)
print('Введите координаты точки B')
b_point = input_data_check(quantity)
print(
    f'Расстояние равно {distance_calculation(a_point, b_point)} между точкой А x ={a_point[0]}, y ={a_point[1]} и точкой В x ={b_point[0]}, y ={b_point[1]}')
