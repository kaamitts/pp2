#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.
import os
def check_exist(path):
    if os.path.exists(path):
        print("Путь существует.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Название файла:", filename)
        print("Путь к каталогу:", directory)
    else:
        print("Путь не существует")
path = input("Введите путь: ")
check_exist(path)