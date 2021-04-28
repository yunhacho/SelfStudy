from collections import deque

N, M = list(map(int, input().split()))
gmap=[list(map(int, input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]

pathqueue=deque([[0,0]])
visited[0][0]=1
dx, dy=[-1,1,0,0],[0,0,-1,1]

while pathqueue:
    posy, posx = pathqueue.popleft()
    if posy==N-1 and posx==M-1:
        print(visited[posy][posx])
        break
    for i in range(4):
        nexty=posy+dy[i]
        nextx=posx+dx[i]
        if 0 <= nexty <= N-1 and 0 <= nextx <= M-1:
            if visited[nexty][nextx]==0 and gmap[nexty][nextx]==1:
                visited[nexty][nextx]=visited[posy][posx]+1
                pathqueue.append([nexty, nextx])
