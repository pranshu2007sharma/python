import math
a = int(input("Enter the coefficient of a"))
b= int(input("Enter the coefficient of b"))
c= int(input("enter the constant"))
d =b**2-4*a*c
if d>=0:
    root1 =(-b+math.sqrt(b**2-4*a*c))/2*a
    root2 =(-b-math.sqrt(b**2-4*a*c))/2*a
    print("ROOTS=", root1, root2)
else:
    print("no real root")