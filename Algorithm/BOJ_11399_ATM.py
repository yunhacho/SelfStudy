N=int(input())
P=list(map(int, input().split()))
total=[0]*N
P.sort()

for i, p in enumerate(P):
    if i==0: total[0]=p
    else: total[i]=total[i-1]+p
print(sum(total))



