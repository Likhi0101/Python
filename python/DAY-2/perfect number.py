a=int(input())
c=0
for i in range (1,a):
    if a%i==0:
        print(i)
        c+=i
if c==a:
    print("perfect")
else:
    print("not a perfect")
