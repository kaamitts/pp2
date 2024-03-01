#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.sub(r"[ ,.]", ":", file)
for i in a:
    print(i, end=" ")