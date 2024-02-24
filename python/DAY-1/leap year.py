a = int(input("enter a year"))
if a%4==0 and a%100!=0:  # we can use a%400==0
    print("leap year")
else:
    print("not a leap year")
