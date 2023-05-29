'''Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных'''

import os

def add_contact(name, surname, phone_number):
    with open('phonebook.txt', 'a') as f:
        f.write(f"{surname} {name} {phone_number}\n")
        print(f"Контакт {name} {surname} добавлен!")

def print_phonebook():
    with open('phonebook.txt', 'r') as f:
        for line in f:
            print(line.strip())

def search_by_name(name):
    with open('phonebook.txt', 'r') as f:
        for line in f:
            if line.split(' ')[1] == name:
                print(line.strip())

def search_by_surname(surname):
    with open('phonebook.txt', 'r') as f:
        for line in f:
            if line.split(' ')[0] == surname:
                print(line.strip())

def search_by_phone_number(phone_number):
    with open('phonebook.txt', 'r') as f:
        for line in f:
            if line.split(' ')[2].strip() == phone_number:
                print(line.strip())

def change_contact(name=None, surname=None, phone_number=None):
    if not any((name, surname)):
        print("Укажите имя или фамилию контакта, которого хотите изменить.")
        return
    need_update = False
    with open('phonebook.txt', 'r') as f, open('new_phonebook.txt', 'w') as new_f:
        for line in f:
            splitted_line = line.split()
            if (name and splitted_line[1] == name) or (surname and splitted_line[0] == surname):
                if phone_number:
                    splitted_line[2] = phone_number
                updated_line = ' '.join(splitted_line) + '\n'
                new_f.write(updated_line)
                need_update = True
                print(f"Контакт {splitted_line[1]} {splitted_line[0]} был успешно изменен!")
            else:
                new_f.write(line)
    os.replace('new_phonebook.txt', 'phonebook.txt')
    if not need_update:
        print("Контакт не найден!")

def delete_contact(name=None, surname=None):
    if not any((name, surname)):
        print("Укажите имя или фамилию контакта, которого хотите удалить.")
        return
    need_update = False
    with open('phonebook.txt', 'r') as f, open('new_phonebook.txt', 'w') as new_f:
        for line in f:
            splitted_line = line.split()
            if (name and splitted_line[1] == name) or (surname and splitted_line[0] == surname):
                need_update = True
                print(f"Контакт {splitted_line[1]} {splitted_line[0]} удален!")
            else:
                new_f.write(line)
    os.replace('new_phonebook.txt', 'phonebook.txt')
    if not need_update:
        print("Контакт не найден!")

def main_menu():
    print("Телефонный справочник")
    print("1. Добавить контакт")
    print("2. Показать все контакты")
    print("3. Поиск по имени")
    print("4. Поиск по фамилии")
    print("5. Поиск по номеру телефона")
    print("6. Изменить данные контакта")
    print("7. Удалить контакт")
    print("0. Выход")

def run():
    while True:
        main_menu()
        choice = input("Введите номер пункта меню: ")
        if choice == '1':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(name, surname, phone_number)
        elif choice == '2':
            print_phonebook()
        elif choice == '3':
            name = input("Введите имя для поиска: ")
            search_by_name(name)
        elif choice == '4':
            surname = input("Введите фамилию для поиска: ")
            search_by_surname(surname)
        elif choice == '5':
            phone_number = input("Введите номер телефона для поиска: ")
            search_by_phone_number(phone_number)
        elif choice == '6':
            name = input("Введите имя для изменения: ")
            surname = input("Введите фамилию для изменения: ")
            phone_number = input("Введите новый номер для телефона: ")
            change_contact(name, surname, phone_number)
        elif choice == '7':
            name = input("Введите имя для удаления: ")
            surname = input("Введите фамилию для удаления: ")
            delete_contact(name, surname)
        elif choice == '0':
            break
        else:
            print("Некорректный ввод! Попробуйте еще раз.")

if __name__ == '__main__':
     run()
