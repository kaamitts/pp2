#Write a Python program to split a string at uppercase letters.
import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.split(r"(?=[A-ZА-Я])", file)
for i in a:
    print (i, end=" ")