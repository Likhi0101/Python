n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
    for j in l:
        if i-j==k:
           flag=1
if flag==1:
    print(True)
else:
    print(False)

