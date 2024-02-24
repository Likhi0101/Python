class A:
    def hi(self):
        print("Hi")
    def hi(self,data):
        print("Hello")
class B:
    def hi(self,data):
        print("Hi")
a=A()
b=B()
a.hi(4)
b.hi(5)
