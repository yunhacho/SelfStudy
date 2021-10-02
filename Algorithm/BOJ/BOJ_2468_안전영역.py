import sys
from collections import deque

def get_secure_area(limit):
    visited=[[False]*n for _ in range(n)]
    dx,dy=[1,-1,0,0], [0,0,-1,1]
    count=0

    def bfs(i,j):
        visited[i][j]=True
        q=deque([(i,j)])
        while q:
            x,y=q.popleft()
            for i in range(4):
                mx,my=x+dx[i], y+dy[i]
                if 0<=mx<n and 0<=my<n and graph[mx][my]>limit and not visited[mx][my]:
                    visited[mx][my]=True
                    q.append((mx,my))
    count=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>limit and not visited[i][j]:
                bfs(i,j)
                count+=1            
    return count

n=int(sys.stdin.readline())
max_amount=0
graph=[]
for _ in range(n):
    row=list(map(int, sys.stdin.readline().split()))
    max_amount=max(max_amount, max(row))
    graph.append(row)

max_area=0
for limit in range(max_amount+1):
    max_area=max(max_area, get_secure_area(limit))
print(max_area)