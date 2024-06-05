import sys

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt') #буферная переменная, которая из функции рид возвратила список в списке - наш справочник
    #print(phone_book)
    while (choice != 8):
        if choice == 1:
            print_result('phonebook.txt')
        elif choice == 2:
            #last_name = input('Введите фамилию абонента ')
            #print(find_user(phone_book,last_name,0))
            print(find_lastname(phone_book))
        elif choice == 3:
            #number_name = input('Введите номер абонента ')
            #print(find_user(phone_book,number_name,2))
            print(find_number(phone_book))
        elif choice==4:
            add_user(phone_book)
            write_txt('phonebook.txt',phone_book)
        elif choice==5:
            print(write_txt('phonebook.txt',phone_book))
        elif choice==6:
             copy_phone_line(phone_book,'phonebook_new.txt')           
        elif choice == 7:            
            choice = out_confirmation()

        choice=show_menu()

#Дополнить справочник возможностью копирования данных из одного файла в другой. 
#Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

def copy_phone_line(phone_book,filename_new):
    number_copy = int(input("Введите номер строки копирования: ")) - 1
    for i in range(len(phone_book)):
        if i == number_copy:
            with open(filename_new,'w',encoding='utf-8') as phout_new:
                s = phone_book[i]
                #for v in phone_book[i].values():
                #    s = s + v + ','
                #phone_book.append(s)
                phout_new.write(f'{s}\n')
                print('Строка', i+1 , 'записана v новый файл') 


def print_result(filename):
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            print(line, end='')

# другая версия поиска (одна функция на оба поиска с флагом)

# def find_user(phone_book, value, flag):
#     if flag == 0: print("Ищем по фамилии")
#     else: print("Ищем по номеру")
#     for i in range(len(phone_book)):
#         if [_ for _ in phone_book[i].values()][flag] == value:
#             res = "---------------\n"
#             for res1, res2 in phone_book[i].items():
#                 res = f'{res}{res1}:{res2} \n'
#             res = f'{res} -----------------\n'
#     if res == '': res = 'абонент не найден \n'
#     return res

def find_lastname(phone_book):
    last_name = input ("Введите фамилию : ")
    res = "---------------\n"
    for i in range(len(phone_book)):
        if phone_book[i]["ФАМИЛИЯ"] == last_name:
            res = phone_book[i]          
    if res == "---------------\n":
        print("Абонент не найден")
    return res

def find_number(phone_book):
    phone_name = input ("Введите номер : ")
    res = "---------------\n"
    for i in range(len(phone_book)):
        if phone_book[i]["ТЕЛЕФОН"] == phone_name:
            res = phone_book[i]  
    if res == "---------------\n":
        print("Абонент не найден") 
    return res

def add_user(phone_book):
    user_data=input('Введитеданные нового абонента через запятую ')
    fields=['ФАМИЛИЯ', 'ИМЯ', 'ТЕЛЕФОН', 'ОПИСАНИЕ']
    record = dict(zip(fields, user_data.split(",")))
    phone_book.append(record)
    return record

def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')
    print("Справочник перезаписан")

def out_confirmation():
    print("Закрыть?")
    confirmation = input("Введите да, если необходимо закрыть программу ")
    if confirmation == "да":
        print("OK, Программа закрывается")
        sys.exit()
    else:
        print("Хорошо, продолжаем ")
        show_menu()

def read_txt(filename): 
    phone_book = []
    fields=['ФАМИЛИЯ', 'ИМЯ', 'ТЕЛЕФОН', 'ОПИСАНИЕ']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            line = line.replace("\n","") #Igor
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book

def show_menu():
    print("\n ВЫБЕРИ ДЕЙСТВИЕ:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в тхт\n"
          "6. Записать абонента вдругой файл\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

work_with_phonebook()