n=int(input("Enter any year="))
if n%400==0 or n%100!=0 and n%4==0:
    print("Leap Year")
else:
    print("Not a leap year")