def palindrome(n):
      s=str(n)
      if s==s[::-1]:
          return 1
      else:
          return 0
n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)            #flag is just a variable and shows some status
    if flag==1:
        l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l1)
print(sum(l2))
