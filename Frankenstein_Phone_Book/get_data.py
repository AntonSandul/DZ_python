# Формируем строку новых данных для записи, которые вводит пользователь 

from writing_to_files import last_key

def data_entry():
    names = []
    last_names = []      
    contact = []
    position =[]
    des = []

    while True:
        last_name = input("Введите фамилию или 'end' для окончания ввода: ")
        if last_name == 'end':
            break
        name = input("Введите имя: ")
        last_names.append(last_name)
        position = input("Введите должность сотрудника: ")
        contact = input("Введите номер телефона: ")
        info = input("Введите комментарий: ")
        position.append(position)
        names.append(name)
        contact.append(contact)
        des.append(info)

    db = {}
    key_start = last_key()
    for i in range(key_start - 1, len(last_names) + key_start):
        key = i + 1
        db[key] = []
        db[key].append(last_names[i])
        db[key].append(names[i])
        db[key].append(contact[i])
        db[key].append(des[i])
        
    return db

    

