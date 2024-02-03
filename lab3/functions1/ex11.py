#Write a Python function that checks whether a word or phrase is palindrome or not. 
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def k(str1):
    str2 = str1[::-1]
    if str1 == str2:
        return "This word is palindrome"
    return "This word is not palindrome"
str1 = str(input())
print(k(str1))