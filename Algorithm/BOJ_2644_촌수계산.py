from collections import deque

N=int(input())
AX, AY=list(map(int, input().split()))
T=int(input())

graph=[[] for _ in range(N+1)]
for _ in range(T):
    x, y=list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

queue=deque([AX])
visited=[]
depths=[0]*(N+1)

while queue:
    node=queue.popleft()
    visited.append(node)
    if node==AY: break

    for fnode in graph[node]:
        if fnode not in visited:
            depths[fnode]=depths[node]+1
            queue.append(fnode)
    
print(depths[AY] if depths[AY]!=0 else -1)
