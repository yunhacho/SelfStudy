# BOJ 1753 최단경로
import sys
import heapq
input=sys.stdin.readline

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(distance[start], start))
    while q:
        dist_of_node, node = heapq.heappop(q)
        if distance[node] < dist_of_node: continue
        for adj, d in graph[node]:
            cost=distance[node]+d
            if distance[adj]>cost:
                distance[adj]=cost
                heapq.heappush(q,(distance[adj],adj))

if __name__=="__main__":
    v,e=map(int, input().split())
    start=int(input())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        f, t, d = map(int, input().split())
        graph[f].append((t,d))
    distance=[int(1e9)]*(v+1)
    dijkstra(start)

    for d in distance[1:]:
        if d==int(1e9): print('INF')
        else: print(d)