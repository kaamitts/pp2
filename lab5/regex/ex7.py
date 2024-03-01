#Write a python program to convert snake case string to camel case string.
def snake_to_camel(snake_str):
    components = snake_str.split("_")
    return components[0]+"".join(x.title for x in components [1:])
import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
    
camel_case_string = snake_to_camel(file)
print(camel_case_string)