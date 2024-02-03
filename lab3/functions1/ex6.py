def k(string1):
    string2 = ' '.join(reversed(string1))
    return string2
string1 = input().split()
print(k(string1))