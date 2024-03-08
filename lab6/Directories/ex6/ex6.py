import os

def generate_files():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in alphabet:
        filename = letter + ".txt"
        with open(filename, "w") as file:
            file.write("This is file " + filename)

if __name__ == "__main__":
    generate_files()