a=int(input())
temp=a
sum=0
while a>0:
    digit=a%10
    sum=sum+digit**3
    a//=10
if sum==temp:
    print("armstrong")
else:
    print("not a armstrong")
    
    
