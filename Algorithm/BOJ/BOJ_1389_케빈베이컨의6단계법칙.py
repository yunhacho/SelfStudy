import sys
from collections import deque

def bfs(v):
    count=0
    q=deque([(v,0)])
    visited=[False]*(n+1)
    
    while q:
        v, depth = q.popleft()
        if not visited[v]:
            for adj in graph[v]:
                if not visited[adj]:
                    q.append((adj,depth+1))
            visited[v]=True
            count+=depth
    return count

n,m=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

print(sorted([(i,bfs(i)) for i in range(1,n+1)], key=lambda x: (x[1],x[0]))[0][0])
