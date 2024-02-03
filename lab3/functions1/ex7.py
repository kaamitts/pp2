def k(list):
    a = True
    for x in range(len(list)-1):
        if int(list[x]) == 3 and int(list[x+1]) == 3:
            return True
    return False
list = list(input().split())
print(k(list))