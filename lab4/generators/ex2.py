#Write a program using generator to print the even numbers 
#between 0 and n in comma separated form where n is input from console
def even_numbers(n):
    for x in range(1, n+1):
        if x%2==0:
            yield x
n = int(input("Введите число: "))
even = even_numbers(n)
try:
    next_even = next(even)
    while True:
        print(next_even, end="" )
        next_even = next(even)
        print(", " if next_even is not None else "", end="")
except StopIteration:
    pass