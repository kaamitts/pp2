#Write a Python program to calculate the area of regular polygon.
import math

number_sides = int(input("Input number of sides: "))
lenght_side = int(input("Input the length of a side: "))
semiperimeter = ((lenght_side*number_sides)/2)
print(semiperimeter)
#Area = math.sqrt(semiperimeter*((semiperimeter-lenght_side)**number_sides))
#print(f"The area of the polygon is: {Area}")