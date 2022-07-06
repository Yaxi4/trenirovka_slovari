a = input().lower()
b = {}
from string import ascii_lowercase

count = 0
for i in a:
    if i in ascii_lowercase:
        if b.get(i) == None:
            b[i]=1
        else:
            b[i]+=1

print(b)
