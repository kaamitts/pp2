#Implement a generator that returns all numbers from (n) down to 0.
def k(n):
    while n>=0:
        yield n
        n -= 1
n = int(input("Ведите число: "))
generator = k(n)
for i in generator:
    print(i, end="")
    if i != 0:
        print(", ", end="")