from datetime import datetime

def input_text():
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    return f"{date};{input('Введите заголовок: ').capitalize()};{input('Введите описание: ')}"

def input_index():
    while True:
        try:
            line_index = input("Введите номер заметки (ID): ")
            if line_index.isdigit:
                return int(line_index)
            else:
                print("!! Некорректный ввод, попробуйте снова !!")
        except ValueError:
            print("!! Неверное значение, попробуйте снова !!")

def input_data():
    while True:
        try:
            date = input("Введите дату в формате дд.мм.гггг: ")
            form = '%d.%m.%Y'
            res = bool(datetime.strptime(date, form))
            if res == True:
                return date
            else:
                print("!! Некорректный ввод, попробуйте снова !!")
        except ValueError:
            print("!! Неверное значение, попробуйте снова !!")

def print_notes(i, line):
    note = line.split(";")
    t1 = note[0]
    t2 = note[1]
    t3 = note[2]
    return print(f"\nID заметки: {i}\nДата создания: {t1}\nЗагаловок: {t2}\nОписание: {t3}")

def print_menu(f):
    if f == "main":
        main: str = """
--= Главное меню =--
1 - показать заметки
2 - добавить заметку
3 - изменить заметку
4 - удалить заметку
5 - выход из приложения"""
        return print(main)
    
    if f == "search":
        search: str = """
Q  Поиск заметки  Q
1 - показать все заметки
2 - найти заметку по Id
3 - найти заметку по дате
4 - назад в главное меню"""
        return print(search)
    
    if f == "remove":
        remove: str = """
- Удаление заметки -
1 - удалить все заметки
2 - удалить заметку по Id
3 - удалить заметки по дате
4 - назад в главное меню
(Учитывайте, что ID заметок
 после удалённой изменится!)"""
        return print(remove)