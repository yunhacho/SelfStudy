# 방문하지않은 노드 중 최단 경로가 가장 짧은 다음 노드 선택 시 
# 순차탐색이 아닌 우선순위큐를 이용해 O(NlogN) 시간복잡도로 개선
import sys
import heapq
input=sys.stdin.readline

def dijkstra(start):
    queue=[]
    distance[start]=0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node=heapq.heappop(queue)
        if distance[node] < dist: continue
        for vto, d in graph[node]:
            cost=dist+d
            if cost < distance[vto]:
                distance[vto]=cost
                heapq.heappush(queue, (cost,vto))
    return distance[1:]


v, e = map(int, input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    vfrom, vto, d = map(int, input().split())
    graph[vfrom].append((vto, d))

distance=[int(1e9)]*(v+1)
print(dijkstra(start))