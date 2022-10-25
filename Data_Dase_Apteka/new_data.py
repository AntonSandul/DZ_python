# Запись данных в файл
def adding():
    to_add = []
    print("\nВы добавляете информацию в базу.\n")
    to_add.append(input('Имя: '))
    to_add.append(input('Фамилия: '))
    to_add.append(input('Должность: '))
    to_add.append(input('Телефон: '))
    to_add.append(input('Коментарий: '))
    with open('last_key.txt', "r") as my_f:
        last_key = my_f.readline().split()
        new_key = int(last_key[-1])
    with open('Data_Base.csv', "a", encoding='utf-8') as base:
        base.write('{},{},{},{},{},{}\n\n'.format(new_key + 1, to_add[0], to_add[1], to_add[2], to_add[3], to_add[4]))
    
    with open('last_key.txt', "w", encoding='utf-8') as my_f:
        my_f.write(f"last_key = {new_key + 1}")
    return to_add