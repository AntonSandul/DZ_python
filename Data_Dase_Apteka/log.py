from datetime import datetime
from time import time


def start_app():  # Старт работы
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('{} Time {}\n'.format('Start work with app', time_calc))


def error_enter(): # Ошибка ввода данных
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('{} Time {}\n'.format('Enter error', time_calc))


def show_all(): # Запрос на отображение всех записей
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('{} Time {}\n'.format('Showed all items', time_calc))


def search(search_object): # Поиск контактов
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('Search: {} Time {}\n'.format(search_object, time_calc))


def add(added_object): # Добавление новой записи
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('Added: {} Time {}\n'.format(added_object, time_calc))


def change(changed_object): # Изменение данных
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('Changed: {} Time {}\n'.format(changed_object, time_calc))


def del_item(deleted_object): # Удаление записи
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('Deleted: {} Time {}\n'.format(deleted_object, time_calc))


def end_app(): # Завершение работы приложения
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write('{} Time {}\n'.format('End work with app', time_calc))