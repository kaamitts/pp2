#Write a Python program to convert degree to radian.
import math
user_degree = float(input("Input degree: "))
user_degree = float((user_degree * math.pi)/180)
print(f"Output radian: {user_degree}")