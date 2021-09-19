from collections import deque

#BOJ 14502
def bfs(x,k,tree):
    queue=deque()
    distance=[-1]*len(tree)
    queue.append(x)
    distance[x]=0

    while queue:
        node=queue.popleft()
        for adj in tree[node]:
            if distance[adj]==-1:
                distance[adj]=distance[node]+1
                queue.append(adj)
    return sorted([node for node, dist in enumerate(distance) if dist==k])
    

if __name__=="__main__":
    n, m , k, x = map(int, input().split())
    tree=[[] for _ in range(n+1)]
    for _ in range(m):
        f, t = map(int, input().split())
        tree[f].append(t)

    result=bfs(x,k,tree)
    if result:print(*result, sep='\n')
    else: print(-1)