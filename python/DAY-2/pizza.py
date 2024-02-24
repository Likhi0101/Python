a,b, = map(int,input().split(" "))
ns=(a*b)
if ns%4==0:
    np = ns//4
else:
    np = ((ns//4)+1)
print(np)


  ''' import math
      a,b, = map(int,input().split(" "))
      ns=(a*b)
      np = math.ceil(c/4)
      print(np) '''
