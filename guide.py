import os 

def get_user_data() -> list:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    tel_number = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name, surname, tel_number, desc] 

def create_record(gb_phone_book:list, user_data:list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book

def print_phone_book(gb_phone_book:list) -> None:
    for user in gb_phone_book:
        print(user)

def get_file_name() -> str:
    return input('Введите имя файла: ')

def import_data(gb_phone_book:list, file_name:str, delimetr:str ) -> list:
    path_source = os.path.join('.', file_name)
    with open(path_source, 'r', encoding='utf8') as source: 
        for line in source:
            gb_phone_book = create_record(gb_phone_book,line.strip().split(delimetr))
    return gb_phone_book   

def search_phone_book() -> str:
    surname_1 = input('Введите фамилию или её первые буквы: ')
    return surname_1
    
def find_record_in_FB(gb_phone_book: list, search_phone_book: str) -> int: 
    for idx in range(len(gb_phone_book)): 
        if ','.join(gb_phone_book[idx]).startswith(search_phone_book)==True: 
            return idx 
    return 1000000000

def export_data(l):
    with open('phone.csv' , 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data

def get_string(message:str) -> str: 
    return input(message)

def delete_person(name):
    persons = get_string(name)
    with open('book.csv', "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def menu():
    phone_book = list()
    while True:
        print('Введите 1 для выхода ')
        print('Введите 2 для добавления новой записи ')
        print('Введите 3 для вывода телефонной книги ')
        print('Введите 4 для импорта данных из файла ')
        print('Введите 5 для поиска человека в списке ')
        print('Введите 6 для экспорта данных в файл ')
        print('Введите 7 для удаления контакта')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print('Вы выбрали выход')
            return 
        if choise == 2:
            phone_book = create_record(phone_book,get_user_data())
        if choise == 3:
            print_phone_book(phone_book)
        if choise == 4:
            phone_book = import_data(phone_book, get_file_name(), ',')
        if choise == 5: 
            record_fnd=find_record_in_FB(phone_book,search_phone_book) 
            if record_fnd!=1000000000: 
                print(phone_book[record_fnd]) 
            else: 
                print("Запись не найдена")
        if choise == 6:
            phone_book = export_data(phone_book)
        if choise == 7:
            phone_book = delete_contact(phone_book, get_string())


menu()