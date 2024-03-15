import os

def list_directories_and_files(path):
    directories = []
    files = []

    # Получаем список всех файлов и каталогов в указанном пути
    items = os.listdir(path)

    # Разделяем файлы и каталоги
    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        else:
            files.append(item)

    return directories, files

path = input("Введите путь: ")
directories, files = list_directories_and_files(path)

print("Каталоги:")
for directory in directories:
    print(directory)

print("\nФайлы:")
for file in files:
    print(file)