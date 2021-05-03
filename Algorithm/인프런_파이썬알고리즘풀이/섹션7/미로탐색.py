SIZE=7
maze=[list(map(int, input().split())) for _ in range(SIZE)]
cnt=0

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dfs(y,x):
    global cnt
    if y==SIZE-1 and x==SIZE-1:
        cnt+=1; return

    for i in range(4):
        nexty, nextx=y+dy[i], x+dx[i]
        if 0<=nexty<SIZE and 0<=nextx<SIZE:
            if maze[nexty][nextx]==0:
                maze[nexty][nextx]=1
                dfs(nexty, nextx)
                maze[nexty][nextx]=0


maze[0][0]=1
dfs(0,0)
print(cnt if cnt>0 else -1)