from string import ascii_lowercase
a={}
count=0
for i in ascii_lowercase:
    a[i]=count+1
    count+=1
for i in a:
    print(i, a.get(i))