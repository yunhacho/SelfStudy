from itertools import product
N, M=list(map(int,input().split()))

comb=[list(range(1,N+1)), list(range(1,M+1))]
sumlst=[[0,0] for _ in range(N+M+1)]

for case in product(*comb):
    total=sum(case)
    sumlst[total][0]+=1
    sumlst[total][1]=total

sumlst.sort(key=lambda x: -x[0])
res=[]
maxcnt, total=sumlst[0][0], sumlst[0][1]
res.append(total)

for count, total in sumlst[1:]:
    if count==maxcnt: res.append(total)
    else: break

print(*res, sep=' ')
