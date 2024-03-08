#Write a Python program to copy the contents of a file to another file
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("Содержимое файла успешно скопировано.")
    except FileNotFoundError:
        print("Исходный файл не найден.")
    except IOError:
        print("Ошибка при копировании содержимого файла.")

if __name__ == "__main__":
    source_file = input("Введите путь к исходному файлу: ")
    destination_file = input("Введите путь к новому файлу: ")
    copy_file(source_file, destination_file)