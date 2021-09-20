# BOJ 1504 특정한 최단 경로
import sys
from heapq import heappush, heappop
input=sys.stdin.readline

def dijkstra(start,n):
    distance=[int(1e9)]*(n+1)
    distance[start]=0
    q=[]
    heappush(q,(distance[start], start))
    while q:
        dist_of_node, node = heappop(q)
        if distance[node] < dist_of_node: continue
        for adj, d in graph[node]:
            cost=distance[node]+d
            if distance[adj]>cost:
                distance[adj]=cost
                heappush(q,(distance[adj], adj))
    return distance

def solution(start, v1,v2,n):
    dist_from_start=dijkstra(start,n)
    dist_from_v1=dijkstra(v1,n)
    dist_from_v2=dijkstra(v2,n)
    answer=min(dist_from_start[v1]+dist_from_v1[v2]+dist_from_v2[n], dist_from_start[v2]+dist_from_v2[v1]+dist_from_v1[n])
    return answer if answer<int(1e9) else -1

if __name__=="__main__":
    n, e = map(int, input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(e):
        f,t,d=map(int, input().split())
        graph[f].append((t,d))
        graph[t].append((f,d))
    v1, v2=map(int, input().split())
    print(solution(1, v1,v2,n))

