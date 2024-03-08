import os

def write_list_to_file(filename, my_list):
    try:
        with open(filename, 'a') as file:  # Открываем файл в режиме добавления
            for item in my_list:
                file.write(item + '\n')  # Добавляем символ новой строки после каждого элемента
        print("Список успешно добавлен в файл", filename)
    except IOError:
        print("Ошибка записи в файл")

if __name__ == "__main__":
    filename = input("Введите название файла: ")
    my_list = ['apple', 'banana', 'orange']
    write_list_to_file(filename, my_list)