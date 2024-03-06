#Write a Python program with builtin function that returns True if all elements of the tuple are true.
row = list(map(input("Вводите через пробел: ").split))
new_row = tuple(row)
def tr_fl(new_row):
    for i in new_row:
        if i is not True:
            return ("Not true")
        else:
            pass
    return ("True")
print(tr_fl(new_row))