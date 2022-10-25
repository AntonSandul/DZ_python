from os import path
from exceptions import *



def change_data():
    search = data_search()
    file = 'Data_base.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            
            text1 = text.readlines()
            for v in enumerate(text1):
                if search in v:
                    new_data = str(input('Введите данные для замены: '))
                    change = str(search.replace(search, new_data))
                    print(change)   
                    