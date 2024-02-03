#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
#For example, histogram([4, 9, 7]) should print the following:
def k(list1):
    for x in list1:
        a = int(x)
        print("*"*a)
list1 = list(input().split())
k(list1)
