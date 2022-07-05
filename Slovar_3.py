
a=int(input())
baza={}

while a>0:
    a-=1
    b=input()
    if baza.get(b)==None:
        baza[b]=1
        print('OK')
    else:

        print(f'{b}{baza[b]}')
        baza[b] += 1
