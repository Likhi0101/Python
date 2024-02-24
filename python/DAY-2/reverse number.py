a=int(input())
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a//=10
print(rev)
    
''' FOR LOOP '''
''' n=int(input())
    rev=0
    for i in range (n):
      if n>0:
          digit=a%10
          rev=rev*10+digit
          a//=10
      else:
         break
    print(rev) '''
