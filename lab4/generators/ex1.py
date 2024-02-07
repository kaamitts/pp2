def squares_up_to_n(n):
    for x in range(1, n+1):
        if x**2 <= n:
            yield x**2
        else: continue 
n = int(input("Введите число n: "))
sqare = squares_up_to_n(n)
for x in sqare:
    print(x, end=' ')
