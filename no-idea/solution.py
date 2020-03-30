a,b = map(int,input().split())
c = input().split(' ')
d = set(input().split(' '))
e = set(input().split(' '))
g = 0

for i in c:
    if i in d:
        g+=1
    if i in e:
        g-=1
print(g)
