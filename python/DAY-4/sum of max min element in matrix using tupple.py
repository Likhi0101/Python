r,c=int(input("rows: ")),int(input("columns: "))
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
#print(l)
min,max=1000,0
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print(min+max)

