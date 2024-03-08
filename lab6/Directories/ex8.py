#Write a Python program to delete file by specified path.
#Before deleting check for access and whether a given path exists or not.
import os

def delete_file(path):
    if not os.path.exists(path):
        print("Указанный путь не существует.")
        return
    if not os.access(path, os.W_OK):
        print("У вас нет доступа для удаления файла.")
        return
    
    try:
        os.remove(path)
        print("Файл успешно удален.")
    except OSError as e:
        print(f"Ошибка удаления файла: {e}")

if __name__ == "__main__":
    file_path = input("Введите путь к файлу для удаления: ")
    delete_file(file_path)