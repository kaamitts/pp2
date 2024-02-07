#Write a program using generator to print the even numbers 
#between 0 and n in comma separated form where n is input from console
def even_numbers(n):
    for x in range(n+1):
        if x%2==0:
            yield x
        else: continue
n = int(input("Введите число: "))
even = list(even_numbers(n))
print(", ".join(map(str, even)))

"""for i, x in enumerate(even):
    if i == len(even) - 1:
        print(x)
    else: 
        print(x, end=", ")"""