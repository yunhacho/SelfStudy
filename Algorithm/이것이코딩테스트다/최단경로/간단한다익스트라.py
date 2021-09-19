import sys
import heapq
import time
input=sys.stdin.readline


def get_smallest_node():
    min_value=int(1e9)
    index=-1
    for i in range(1,v+1):
        if not visited[i] and min_value>=distance[i]:
            min_value=distance[i]
            index=i
    return index


def dijkstra(start):
    s=time.time()
    visited[start]=True
    distance[start]=0
    for to, d in graph[start]:
        distance[to]=d

    for _ in range(v-1):
        now=get_smallest_node()
        visited[now]=True
        for to, d in graph[now]:
            distance[to]=min(distance[to], distance[now]+d)
    print("linear: ", time.time()-s)
    return distance[1:]

def dijkstraheap(start):
    s=time.time()
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
    print("heapq: ", time.time()-s)
    return distance[1:]

v, e = map(int, input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    vfrom, vto, d = map(int, input().split())
    graph[vfrom].append((vto, d))

visited=[False]*(v+1)
distance=[int(1e9)]*(v+1)
print(dijkstra(start))

distance=[int(1e9)]*(v+1)
print(dijkstraheap(start))

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3 
4 5 1
5 3 1
5 6 2
'''