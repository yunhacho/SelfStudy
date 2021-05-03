from collections import deque

SIZE=7
maze=[list(map(int, input().split())) for _ in range(SIZE)]
visit=[[0]*SIZE for _ in range(SIZE)]
count=[[0]*SIZE for _ in range(SIZE)]

dy=[-1,1,0,0] # 상하좌우
dx=[0,0,-1,1]

queue=deque()
queue.append([0,0])

cango=False
while queue:
    y,x=queue.popleft()
    if y==SIZE-1 and x==SIZE-1:
        cango=True; break
    visit[y][x]=1
    for i in range(4):
        nexty, nextx=y+dy[i], x+dx[i]
        if 0<=nexty<SIZE and 0<=nextx<SIZE:
            if maze[nexty][nextx]==0 and visit[nexty][nextx]==0:
                visit[nexty][nextx]=1
                count[nexty][nextx]=count[y][x]+1
                queue.append([nexty, nextx])

print(count[SIZE-1][SIZE-1] if cango else -1)