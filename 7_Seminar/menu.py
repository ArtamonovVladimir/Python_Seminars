from actions import search, add_record, delete_record, print_phones, input_data_check
from log import log_record, opens, recording


def print_menu():
    print('Введите 1 для Вывода всего телефонного справочника')
    print('Введите 2 для Добавления номера телефона')
    print('Введите 3 для Удаления записи из справочника')
    print('Введите 4 для Поиска номера телефона')
    print('Введите 5 для Выхода')
    print()


def start():
    phones = {}
    # phones = opens(phones)
    menu_choice = 0
    print_menu()

    while menu_choice != 5:
        print_menu()
        menu_choice = input_data_check()
        if menu_choice == 1:
            print_phones(phones)
        elif menu_choice == 2:
            add_record(phones)
            log_record(phones)
        elif menu_choice == 3:
            delete_record(phones)
            log_record(phones)
        elif menu_choice == 4:
            search(phones)
        elif menu_choice != 5:
            print_menu()
    print(phones)
    recording(phones)
