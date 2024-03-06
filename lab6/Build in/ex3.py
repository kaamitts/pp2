"""Write a Python program with builtin function 
that checks whether a passed string is palindrome or not."""
def polindrome(n):
    if n == reversed(n):
        print("Polindrome")
    else:
        print("Not polindrome")
    
string1 = input()
polindrome(string1)
