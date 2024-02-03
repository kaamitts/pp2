def prime(list1, list2):
    for x in list1:
        x = int(x)
        if x < 2:
            continue
        is_prime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break 
        if is_prime:
            list2.append(x)
    return list2
list1 = list(input().split())
list2 = []
print (prime(list1, list2))