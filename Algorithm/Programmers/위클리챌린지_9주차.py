from collections import deque

solution=lambda n,wires: min(bfs(n,wires, wire) for wire in wires)

def bfs(n, wires, wire):
    tree=[[] for _ in range(n+1)]
    for a,b in wires:
        if a==wire[0] and b==wire[1]: continue
        tree[a].append(b); tree[b].append(a)       
    count=0
    q=deque([wire[0]])
    visited=[False]*(n+1)
    while q:
        v=q.popleft()
        if not visited[v]:
            visited[v]=True
            count+=1
            q.extend(tree[v])
    return abs((n-count)-(count))