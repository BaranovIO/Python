# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных



def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}' 
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list
        

def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)

def search_contact(f):
    print('По какому параметру хотите найти контакт?\n'
            '1 - Имя;\n'
            '2 - Фамилия;\n'
            '3 - Номер;\n')
    search_choice = int(input('Введите параметр поиска: '))
    if search_choice == 1:
        parameter_of_search = input('Введите имя: ')
    if search_choice == 2:
        parameter_of_search = input('Введите фамилию: ')
    if search_choice == 3:
        parameter_of_search = input('Введите номер: ')
    adr_book = read_all(f)
    for line in adr_book:
        if parameter_of_search in line:
            print(line)


# def update_contact(f):
#     name = input('Введите имя или фамилию контакта, который хотите изменить: ')
#     new_phone = input('Введите новый номер телефона: ')
    
#     with open('address_book.txt', 'r', encoding='utf-8') as fd:
#         lines = fd.readlines()
    
#     found = False
    
#     with open('address_book.txt', 'w', encoding='utf-8') as fd:
#         for line in lines:
#             if name in line:
#                 fd.write(f"{line.split(';')[0]} : {new_phone}\n")
#                 found = True
#             else:
#                 fd.write(line)
    
#     if found:
#         print('Контакт успешно изменен.')
#     else:
#         print('Контакт не найден.')


def delete_contact(f):
    name = input('Введите имя или фамилию контакта, который хотите удалить: ')
    
    with open('address_book.txt', 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    
    found = False
    
    with open('address_book.txt', 'w', encoding='utf-8') as fd:
        for line in lines:
            if name not in line:
                fd.write(line)
            else:
                found = True
    
    if found:
        print('Контакт успешно удален.')
    else:
        print('Контакт не найден.')
    
    
def main():
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить имя,\n2 - прочитать всю телефонную книгу,\n'
                            '3 - найти запись,\n4 - изменить номер телефона,\n'
                            '5 - удалить запись,\nz - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            update_contact(file)
        elif user_choice == '5':
            delete_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего!')
        break

        
    

if __name__ == '__main__':
    main()

