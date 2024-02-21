#Create a generator that generates the squares of numbers up to some number N.

def squares_up_to_n(n):
    for x in range(1, n+1):
        if x**2 <= n:
            yield x**2
        else: continue 
n = int(input("Введите число n: "))
square = squares_up_to_n(n)
try:
    while True:
        print(next(square), end=', ')
except StopIteration:
    pass