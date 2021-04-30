from collections import deque

M, N, H=list(map(int, input().split()))
boxs=[[list(map(int, input().split())) for n in range(N)] for h in range(H)]
visit=[[[0]*M for n in range(N)] for h in range(H)]

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]


queue=deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxs[z][y][x]==1:
                queue.append([z,y,x])

while queue:
    z,y,x=queue.popleft()
    visit[z][y][x]=1

    for i in range(6):
        nextx=x+dx[i]
        nexty=y+dy[i]
        nextz=z+dz[i]

        if 0<=nextx<M and 0<=nexty<N and 0<=nextz<H:
            if boxs[nextz][nexty][nextx]==0 and visit[nextz][nexty][nextx]==0:
                boxs[nextz][nexty][nextx]=boxs[z][y][x]+1
                visit[nextz][nexty][nextx]=1
                queue.append([nextz,nexty,nextx])

dayofall=-1
for box in boxs:
    for line in box:
        for dayoftomato in line:
            if dayoftomato==0:
                print(-1)
                exit(0)
            dayofall=max(dayofall, dayoftomato)

print(dayofall-1 if dayofall!=-1 else -1)
