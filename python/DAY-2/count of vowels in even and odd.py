s=input()
ev,oc=0,0
for i in range(len(s)):
    if i%2==0:
        if s[i] in "aeiouAEIOU":
            ev+=1
    else:
        if s[i] in "aeiouAEIOU":
            oc+=1
print(ev,oc)
