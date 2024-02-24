a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        print(i)
        c++i
if c==2:
        print("prime")
else:
        print("not prime")
  '''
     a=int(input())
     c=0
     for i in range(1,a+1):
        if a%i==0:
            print(i)
            c++i
     if c==2:
            print("prime")
     else:
            print("not prime") '''
  # without count
  '''
     a=int(input())
     for i in range(2,a):
        if a%i==0:
            print(i)
            print("not prime")
            break
     else:
            print("prime") '''
  '''
     a=int(input())
     for i in range(2,(a//2)+1):
        if a%i==0:
            print(i)
            print("not prime")
     else:
            print("prime") '''
  '''
     a=int(input())
     for i in range(2,(a**0.5)+1):
        if a%i==0:
            print(i)
            print("not prime")
     else:
            print("prime") '''
  '''
    a=int(input())
    i=2
     while i < (2,(a**0.5)+1):
        if a%i==0:
            print(i)
            print("not prime")
        i+=1
     else:
            print("prime") '''
