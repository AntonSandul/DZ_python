
from os import path
from exceptions import data_search, user_choice


def look():  
    search = data_search()
    file = 'Data_Base.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text: 
            count = False
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):  
                if search in v:
                    print('Данные из базы в фаиле Data_Base.csv')
                    print(v.strip())
                    count = True
            if not count: print('Таких данных нет в справочнике фаила Data_Base.csv') 
            return v.strip() 

def delete_contact():
    look()
    print('Введите номер записи, которую хотите удалить:\n')
    del_key = user_choice()
    with open('Data_Base.csv', 'r', encoding='utf-8') as data:
        contact = data.readlines()
        with open('Data_Base.csv', 'w', encoding='utf-8') as data:
            for i in range(len(contact)):
                if i != del_key:
                    data.write(contact[i])