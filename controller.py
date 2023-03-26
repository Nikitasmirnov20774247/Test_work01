from functions import print_menu, input_text, input_index, input_data
from file_oper import *

def run():
    choice = ""
    while choice != "5":
        print_menu("main")
        choice = input("Введите пункт меню: ").strip()
        if choice == '1':
            search_run()
        if choice == '2':
            write_file(input_text())
        if choice == '3':
            index = input_index()
            if check_file() == True and check_line(index) == True:
                replace_notes(index, input_text())
        if choice == '4':
            remove_run()
        if choice == '5':
            print("\n*Выход из приложения*")
            return

def search_run():
    choice = ""
    while choice != "4":
        print_menu("search")
        choice = input("Введите пункт меню: ").strip()
        if choice == '1':
            if check_file() == True:
                read_notes()
        if choice == '2':
            index = input_index()
            if check_file() == True and check_line(index) == True:
                read_notes_id(index)
        if choice == '3':
            if check_file() == True:
                read_notes_data(input_data())
        if choice == '4':
            print("\n*Возвращаемся в главное меню*")
            return choice == ""

def remove_run():
    choice = ""
    while choice != "4":
        print_menu("remove")
        choice = input("Введите пункт меню: ").strip()
        if choice == '1':
            if check_file() == True:
                remove_notes_all()
        if choice == '2':
            index = input_index()
            if check_file() == True and check_line(index) == True:
                remove_notes(index)
        if choice == '3':
            if check_file() == True:
                remove_notes_date(input_data())
        if choice == '4':
            print("\n*Возвращаемся в главное меню*")
            return choice == ""