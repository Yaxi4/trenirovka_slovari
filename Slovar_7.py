s1=input()
s2=input()
a1={}
a2={}
for i in s1:
    if a1.get(i)==None:
        a1[i]=1
    else:
        a1[i]+=1
for i in s2:
    if a2.get(i) == None:
        a2[i] = 1
    else:
        a2[i] += 1
if a1==a2:
    print('Yes')
else:
    print('No')