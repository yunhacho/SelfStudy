import sys
from collections import deque

def dfs(v):
    visited[v]=True
    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)

def bfs(v):
    visited[v]=True
    q=deque([v])
    while q:
        node=q.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj]=True
                q.append(adj)

n,m=map(int,sys.stdin.readline().split())
visited=[False]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)