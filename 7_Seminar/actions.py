def input_data_check():
    i = True
    while i:
        try:
            input_number = int(
                input('Введите команду: '))
            i = False
        except ValueError:
            print('Ввод данных не верен, повторите ввод!')
    return input_number


def print_phones(phones):
    print("Текущие записи:")
    for i in phones.keys():
        print(f'ФИО:  {i}, Номер: {phones[i]}')


def add_record(phones):
    print("Добавление записи")
    name = input("ФИО: ")
    phone = input("Номер: ")
    phones[name] = phone


def delete_record(phones):
    print("Удаление записи из справочника")
    name = input("ФИО: ")
    if name in phones:
        del phones[name]
    else:
        print(name, "Не найдено")
    return phones


def search(phones):
    print("Поиск номера телефона")
    name = input("ФИО: ")
    if name in phones:
        print(f'Номер телефона:  {phones[name]}')
    else:
        print(name, "Не найдено")
