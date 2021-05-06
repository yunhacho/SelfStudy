N=int(input())
pixel=[list(map(int, input().split())) for _ in range(N)]

rowsum=[0]*N
colsum=[0]*N
xsum=[0]*2
for row in range(N):
    rowsum[row]=sum(pixel[row])
    for col in range(N):
        colsum[col]+=pixel[row][col]
        if row==col:
            xsum[0]+=pixel[row][col]
            xsum[1]+=pixel[row][-1-col]

maxs=max(max(rowsum), max(colsum))
maxs=max(maxs, max(xsum))
print(maxs)