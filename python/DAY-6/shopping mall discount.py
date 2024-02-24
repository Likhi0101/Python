#shopping mall have 5%discount for men and 7%discount for women and individual discount for each item they purchase is 3*number of items they purchase calculate the total bill.
n=int(input("Enter no of items: "))
d={}
for i in range(n):
    key = input("items:")
    value = int(input("price:"))
    d[key]= value
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter gender:")
if g == "male":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items-price:discount-price")
for i in d:
    print(f"(i) {d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"total bill:{bill}")




