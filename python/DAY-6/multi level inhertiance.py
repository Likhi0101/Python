class A:
    def __init__(self,data1):
        self.data1=data1
        print("data 1",data1)
class B(A):
    def __init__(self,data2):
        super().__init__(self.data1)
        print("data 2",data2)
class C(B):
    def __init__(self,data1,data2,data3):
        self.data1=data1
        self.data2=data2
        super().__init__(self.data1,self.data2)
        self.data3=data3
        print("data 3",data3)
a,b,c=map(str,input().split())
obj=C(a,b,c)
