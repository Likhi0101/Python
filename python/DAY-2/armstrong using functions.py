def armstrong(a,b):
    for i in range (a,b+1):
        sum=0
        x=i
        while i>0:
            temp=i%10
            sum+=temp**3
            i//=10
        if sum==x:
            print(x)
a,b=int(input()),int(input())
armstrong(a,b)
    
