#Write a function that takes in a list of integers and returns True if it contains 007 in order
def k(list1):
    con = True
    a = 0
    b = 0
    c = 0
    if '0' in list1:
        a = int(list1.index('0'))
        list1.pop(a)
    if '0' in list1:
        b = int(list1.index('0'))
        list1.pop(b)
    if '7' in list1:
        c = int(list1.index('7'))
        list1.pop(c)
    if a<b<c or b<a<c:
        return True
    return False
list1 = list(input().split())
print(k(list1))