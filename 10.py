a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
print((a if a>c else c)) if a>b else print(b if b>c else c)