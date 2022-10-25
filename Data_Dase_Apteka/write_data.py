def writing_scv(Data_Base):
    with open('Data_Base.csv', 'a', encoding='utf-8') as data:
        data.write('№,Имя,Фамилия,Должность,Номер телефона,Коментарий\n')
        for v in Data_Base.items():
            data.write(
                f' {last_key()},{v[0]},{v[1]},{v[2]},{v[3]},{v[4]}\n')


def last_key():
    with open('last_key.txt', "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    with open('last_key.txt', "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
    return new_key + 1