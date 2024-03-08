#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
def k(path):
    directories= []
    files= []
    items = os.listdir(path)
    
    for item in items:
        full_path =  os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        else:
            files.append(item)
    return directories, files

path = input("Введите путь: ")
directories, files = k(path)
print("Каталоги: ")
for i in directories:
    print(i)
print("\nФайлы: ")
for i in files:
    print(i)