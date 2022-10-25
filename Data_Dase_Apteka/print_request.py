from os import path


def print_csv(): 
    file = 'Data_base.csv'
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as text:
            text_csv = text.readlines()
            for i, v in enumerate(text_csv):
                print(v.strip())

