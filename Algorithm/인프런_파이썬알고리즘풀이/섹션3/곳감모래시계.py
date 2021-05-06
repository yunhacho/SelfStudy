N=int(input())
parm=[list(map(int, input().split())) for _ in range(N)]

for _ in range(int(input())):
    row, d, cnt=list(map(int, input().split()))
    stridx=cnt%N
    if stridx!=0:
        if d==0:
            new=parm[row-1][stridx:]
            new.extend(parm[row-1][0:stridx])
            parm[row-1]=new
        if d==1:
            new=parm[row-1][-stridx:]
            new.extend(parm[row-1][0:-stridx])
            parm[row-1]=new

mid=N//2
count=parm[mid][mid]
for i in range(1,mid+1):
    count+=sum(parm[mid-i][mid-i:mid+i+1])
    count+=sum(parm[mid+i][mid-i:mid+i+1])

print(count)
