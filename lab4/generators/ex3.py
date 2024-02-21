"""Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n."""
def div(n):
    for x in range(1, n+1):
        if x % 3 == 0 and x % 4 == 0:
            yield x
n = int(input("Введите число: "))
div_3_4 = div(n)
try:
    by_3_4 = next(div_3_4)
    while True:
        print(by_3_4, end="")
        by_3_4 = next(div_3_4)
        print(", " if by_3_4 is not None else "", end="")
except StopIteration:
    pass