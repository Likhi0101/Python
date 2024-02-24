a = int(input("number of children"))
b = int(input("number of chocolate"))
if a<b:
    print("0")
else:
    print(a-b)
    packets = (a-b)/4
    print(packets)
