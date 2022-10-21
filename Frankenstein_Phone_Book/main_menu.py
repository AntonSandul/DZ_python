# Главное меню. Управление всеми модулями

from find_data import look, delete_contact
from print_request import print_csv, print_txt, print_all
from exceptions import user_choice
from writing_to_files import writing_txt, writing_scv
import get_data
from add_new_data import adding
import logger


def input_contact_menu_choice():
    logger.start_app()
    while True:
        print()
        print('-----------------------')
        print('= Главное меню =')
        print('-----------------------')
        print()
        print('1. Показать все')
        print('2. Поиск записей')
        print('3. Добавить новую запись')
        print('4. Изменить существующую запись')
        print('5. Удалить запись')
        print('6. Создать новую телефонную книгу')
        print('0. Выход')
        choice_menu = user_choice()
        if choice_menu == 1:
            print('1. вывод данных из файла Phonebook.csv в консоль')
            print('2. вывод данных из файла Phonebook.txt в консоль')
            print('3. запись данных из всех файлов в файл Phonebook_general.csv')
            print('0. Вернуться в главное меню')
            choice1 = user_choice()
            if choice1 == 1:
                print_csv()
                logger.show_all()
            if choice1 == 2:
                print_txt()
                logger.show_all()
            if choice1 == 3:
                print_all()
                logger.show_all()
            else:
                return input_contact_menu_choice()
        elif choice_menu == 2:
            search_object = look()
            logger.search(search_object)
        elif choice_menu == 3:
            to_add = adding()
            logger.add(to_add)
        elif choice_menu == 4:
            return 4
        elif choice_menu == 5:
            del_key = delete_contact()
            logger.del_item(del_key)
        elif choice_menu == 6:
            phonebook = get_data.data_entry()
            writing_scv(phonebook)
            writing_txt(phonebook)
            new_key = max(phonebook)
            with open('last_key.txt', "w", encoding='utf-8') as my_f:
                my_f.write(f"last_key = {new_key}")
            logger.new_book()

        elif choice_menu == 0:
            logger.end_app()
            return exit()
        else:
            return input_contact_menu_choice()


print(input_contact_menu_choice())
