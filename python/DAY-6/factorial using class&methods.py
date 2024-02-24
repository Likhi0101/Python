'''class fact():
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)
obj=fact()
obj.fact(int(input()))'''






class fact():
    def __init__(self,data):
        self.data=data
        self.fact(data)
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)
obj=fact(int(input()))
