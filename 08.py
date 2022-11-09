a=int(input("Enter cofficient of x^2="))
b=int(input("Enter cofficient of x="))
c=int(input("Enter constant value="))
d=b**2-4*a*c
if d>0:
    print("Roots are real and distict")
elif d<0:
    print("Roots are imaginary")
else:
    print("Roots are real and equal")



