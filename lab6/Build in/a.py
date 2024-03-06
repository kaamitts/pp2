def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = list(map(int, input("Введите числа через запятую: ").split(",")))
result = multiply(numbers)
print(result)