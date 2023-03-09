# Задача 38
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def add_users():
    last_name = input("Фамилию: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    phone = input("Телефон: ")
    data = (last_name, first_name, middle_name, phone)
    data_str = ', '.join(map(str, data))
    
    with open('file.txt', 'a', encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')

    data_str = data_str.replace(',', ' ')
    return print(f'Внесён пользователь {data_str}')


def read_file():
    with open('file.txt', 'r', encoding='utf-8') as fd:
        data = fd.readlines()
    
    res = []
    key = ['Фамилия', 'Имя', 'Отчество']
    for item in data:
        res.append(dict(zip(key, item.replace('\n', '').split(sep = ','))))
    
    return res

def find_user():
    data = read_file()
    res = []
    key = ['Фамилия', 'Имя', 'Отчество']
    param = input("Введите параметр для поиска человека: Фамилия, Имя, Отчество, Телефон: ")
    if param in key:
        value = input("Введите значение параметра: ")
        for item in data:
            if item[param].replace(" ", "") == value:
                res.append(item)
    else:
        return print("Неверный параметр")       
    
    if res:
        return res
    else:
        return print("Нет такого человека")

def delete_info():
    param = 'Сидоров'
    # input("Введите значение параметра: ")
    with open('file.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    with open('file.txt', 'w', encoding='utf-8') as fd:
        for value in data:
            if param in value:
                print(value)
                fl = 'да'
                # input("Удалить информацию об этом человеке? да, нет: ")
                if fl == 'да':
                    fl = 'нет'
                    continue
            
            fd.write(value)
            

if __name__ == '__main__':
    # add_users()
    # print(read_file())
    # print(find_user())
    delete_info()