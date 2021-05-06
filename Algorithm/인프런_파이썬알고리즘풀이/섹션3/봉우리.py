N=int(input())
mountain=[list(map(int,input().split())) for _ in range(N)]
mountain.insert(0,[0]*N)
mountain.append([0]*N)
for _ in mountain:_.insert(0,0); _.append(0)

count=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(1,N+1):
    for j in range(1,N+1):
        if all(mountain[i][j] > mountain[i+dy[k]][j+dx[k]] for k in range(4)):
            count+=1
print(count)

'''
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)

N=int(input())
mountain=[list(map(int,input().split())) for _ in range(N)]
start = time.time()
visit=[[0]*N for _ in range(N)]
count=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    for j in range(N):
        if visit[i][j]==0:
            visit[i][j]=1
            isbonguri=True
            for t in range(4):
                y,x=i+dy[t], j+dx[t]
                if 0<=y<N and 0<=x<N:
                    if mountain[y][x] >=mountain[i][j]:
                        isbonguri=False
                    else:
                        visit[y][x]=1
            if isbonguri:
                count+=1

print(count)
'''