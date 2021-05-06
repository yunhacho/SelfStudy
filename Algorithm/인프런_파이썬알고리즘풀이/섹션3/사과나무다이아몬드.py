N=int(input())
parm=[list(map(int, input().split())) for _ in range(N)]
mid=N//2
count=sum(parm[mid])

for i in range(1, mid+1):
    count+=sum(parm[mid-i][i:N-i])
    count+=sum(parm[mid+i][i:N-i])
print(count)