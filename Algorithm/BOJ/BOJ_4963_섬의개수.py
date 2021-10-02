import sys
from collections import deque

def bfs(i,j):
    dx=[-1,1,0,0,1,1,-1,-1]
    dy=[0,0,1,-1,-1,1,-1,1]
    visited[i][j]=True
    q=deque([(i,j)])
    while q:
        x,y=q.popleft()
        for i in range(8):
            mx,my=x+dx[i], y+dy[i]
            if 0<=mx<h and 0<=my<w and graph[mx][my] and not visited[mx][my]:
                visited[mx][my]=True
                q.append((mx,my))

while True:
    w,h=map(int, sys.stdin.readline().split())
    count=0
    if w==0 and h==0: break

    graph=[list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and not visited[i][j]:
                bfs(i,j)
                count+=1
    print(count)