import log 
from new_data import *
from serch_data import *
from print_request import *
from change_data import *
def input_contact_menu_choice():
    log.start_app()
    while True:
        print()
        print('************************')
        print('    = Главное меню =    ')
        print('************************')
        print()
        print('1. Показать все записи')
        print('2. Поиск сотрудника по фамилии')
        print('3. Добавить новую запись')
        print('4. Изменить существующую запись')
        print('5. Удалить запись')        
        print('0. Выход')
        choice_menu = user_choice()
        if choice_menu == 1:
            print('1. вывод данных из файла Data_Base.csv')        
            print('0. Вернуться в главное меню')
            choice1 = user_choice()
            if choice1 == 1:
                print_csv()
                log.show_all()
            else:
                return input_contact_menu_choice()
        elif choice_menu == 2:
            search_object = look()
            log.search(search_object)
        elif choice_menu == 3:
            to_add = adding()
            log.add(to_add)
        elif choice_menu == 4:
            change = change_data()
            log.change(change)
        elif choice_menu == 5:
            del_key = delete_contact()
            log.del_item(del_key)       
        elif choice_menu == 0:
            log.end_app()
            return exit()
        else:
            return input_contact_menu_choice()


print(input_contact_menu_choice())