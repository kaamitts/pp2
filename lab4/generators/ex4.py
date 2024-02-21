"""Implement a generator called squares to yield the square of all numbers from (a) to (b).
Test it with a "for" loop and print each of the yielded values."""
def squares(a,b):
    for x in range(a, b+1):
        yield x**2
a = int(input("ВВедите первое число: "))
b = int(input("ВВедите второе число: "))
n = squares(a,b)
for i in n:
    print(i, end="")
    if i != b**2:
        print(", ", end="")