#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.findall(r"[A-ZА-Я][a-zа-я]+", file)
for i in a:
    print (i, end=" ")