N=int(input())
a=list(map(int, input().split()))
M=int(input())
b=list(map(int, input().split()))

a.extend(b)
print(*sorted(a), sep=' ')

'''
p1=p2=0
c=[]
while p1<N and p2<M:
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<N:
    c.extend(a[p1:])
if p2<M:
    c.extend(b[p2:])

print(*c, sep=' ')
'''