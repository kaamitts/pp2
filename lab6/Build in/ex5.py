#Write a Python program with builtin function that returns True if all elements of the tuple are true.
row = input("Введите элементы через пробел: ").split()
new_row = tuple(row)

def all_true(tup):
    for elem in tup:
        if elem == False:
            return False
    return True

print(all_true(new_row))