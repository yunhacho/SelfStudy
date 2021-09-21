from heapq import heappush, heappop
from collections import deque

def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    for f, t in edge:
        graph[f].append(t)
        graph[t].append(f)
    #distance=dijkstra(1, graph, n)
    distance=bfs(1,graph,n)
    return distance.count(max(distance))

def dijkstra(start, graph, n):
    q=[]
    distance=[int(1e9)]*(n+1)
    distance[start]=0
    heappush(q,(0, start))
    while q:
        dist_of_node, node = heappop(q)
        if dist_of_node > distance[node]: continue
        for adj in graph[node]:
            cost=distance[node]+1
            if distance[adj] > cost:
                distance[adj]=cost
                heappush(q,(cost, adj))
    return distance[1:]

def bfs(start, graph, n):
    distance=[0]*(n+1)
    visited=[False]*(n+1)
    visited[start]=True
    queue=deque([start])
    
    while queue:
        node=queue.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                distance[adj]+=distance[node]+1
                queue.append(adj)
                visited[adj]=True
                
    return distance[1:]