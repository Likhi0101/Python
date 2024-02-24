def composite(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
            return l
    else:
            return 0
a,b=int(input()),int(input())
l=[]
for i in range(a,b+1):
    if i%2!=0:
        flag=composite(i)
        if flag==l:
            l.append(i)
print(sum(l))
print(l)
