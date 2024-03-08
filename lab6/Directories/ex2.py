#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path
import os
def check_access(path):
    if not os.path.exists(path):
        print("Нет доступа")
        return

    if os.access(path, os.R_OK):
        print("Путь доступен для чтения.")
    else:
        print("Путь не доступен для чтения.")
    if os.access(path, os.W_OK):
        print("Путь доступен для записи")
    else:
        print("Путь не доступен для записи")
    if os.access(path, os.X_OK):
        print("Путь доступен для выполнения")
    else:
        print("Путь не доступен для выполнения")
        
if __name__ == "__main__":
    path = input("Введите путь: ")
    check_access(path)