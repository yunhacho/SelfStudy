from heapq import heappush, heappop
def dijstra(graph, c):
    q=[]
    distance=[int(1e9)]*len(graph)
    distance[c]=0
    heappush(q,(0,c))
    while q:
        dist_of_v, v = heappop(q)
        if dist_of_v > distance[v]: continue
        for adj, d in graph[v]:
            cost=distance[v]+d
            if distance[adj]>cost:
                distance[adj]=cost
                heappush(q,(cost, adj))
    d=list(filter(lambda x: x<int(1e9), distance[1:]))
    return len(d)-1, max(d)

if __name__=="__main__":
    v, e, c = map(int, input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        f,t,d=map(int, input().split())
        graph[f].append((t,d))
    cnt, t=dijstra(graph,c)
    print(cnt, t)