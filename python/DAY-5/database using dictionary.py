n=int(input("enter no of students")
m=int(input("enter no of subjects:")
d={}
for i in range(n):
      k=input("enter th roll no:")
      v={}
      for j in range(m):
          sub=input("enter the subject name:")
          marks=int(input("enter marks:"))
          v[sub]=marks
     d[k]=v
print(d)
