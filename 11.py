n=int(input("Enter month number="))
if n in (1,3,5,7,8,10,12):
    print(n,"number month has 31 days")
elif n==2:
    print(n,"number month has 28 or 29 days")
elif n in (4,6,9,11):
    print(n,"number month has 30 days")
else:
    print("Invalid month number")
    