from os import remove, rename, stat, path
from functions import print_notes

def write_file(txt):
    with open('notes.csv', mode="a", encoding='utf-8') as file:
        file.write(f"{txt}\n")
    file.close()

def remove_notes_all():
    with open('notes.csv', mode='w+', encoding='utf-8') as file:
        file.seek(0)
    file.close()

def remove_notes(index):
    index -= 1
    with open('notes.csv', mode='r', encoding='utf-8') as file1, \
            open('notestmp.csv', mode='a', encoding='utf-8') as file2:
        lines = file1.read().strip().split("\n")
        for line in lines:
            if line != lines[index]:
                file2.write(f"{line}\n")
    file1.close()
    file2.close()
    remove('notes.csv')
    rename('notestmp.csv', 'notes.csv')
    print("*Заметка успешно удалена*")

def remove_notes_date(date):
    with open('notes.csv', mode='r', encoding='utf-8') as file1, \
            open('notestmp.csv', mode='a', encoding='utf-8') as file2:
        lines = file1.read().strip().split("\n")
        for line in lines:
            if date not in line:
                file2.write(f"{line}\n")
    file1.close()
    file2.close()
    remove('notes.csv')
    rename('notestmp.csv', 'notes.csv')
    print(f"*Заметки за {date} успешно удалены*")

def read_notes_id(index):
    index -= 1
    i = 0
    with open('notes.csv', mode='r', encoding='utf-8') as file:
        lines = file.read().strip().split("\n")
        for line in lines:
            i += 1
            if line == lines[index]:
                print_notes(i, line)
    file.close()

def read_notes_data(data):
    i = 0
    is_true = False
    with open('notes.csv', mode='r', encoding='utf-8') as file:
        while True:
            i += 1
            line = file.readline()
            if not line:
                break
            if data in line:
                print_notes(i, line)
                is_true = True
        if not is_true:
            print("!! Заметка не найдена !!")
    file.close()

def read_notes():
    i = 0
    with open('notes.csv', mode='r', encoding='utf-8') as file:
        while True:
            i += 1
            line = file.readline()
            if not line:
                break
            print_notes(i, line)
    file.close()

def replace_notes(index, new_line):
    index -= 1
    with open('notes.csv', mode='r', encoding='utf-8') as file1, \
            open('notestmp.csv', mode='a', encoding='utf-8') as file2:
        lines = file1.read().strip().split("\n")
        lines[index] = new_line
        for line in lines:
            file2.write(f"{line}\n")
    file1.close()
    file2.close()
    remove('notes.csv')
    rename('notestmp.csv', 'notes.csv')
    print("*Заметка успешно изменена*")

def check_file():
    if (path.exists('notes.csv') and stat("notes.csv").st_size != 0) :
        return True
    else:
        print('!! Заметок нет, создайте заметку !!\n')
        return False

def check_line(index):
    with open('notes.csv', mode='r', encoding='utf-8') as file:
        lines = file.read().strip().split("\n")
        file.close()
        if (index > len(lines) or index < 1):
            print('!! Заметка не найдена !!')
            return False
        else:
            return True