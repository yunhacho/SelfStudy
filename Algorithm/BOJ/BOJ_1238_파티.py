from heapq import heappush, heappop

def dijstra(graph, start):
    distance=[int(1e9)]*len(graph)
    distance[start]=0
    q=[]
    heappush(q, (0,start))
    while q:
        dist, v = heappop(q)
        if dist > distance[v]: continue
        for adj, d in graph[v]:
            cost=distance[v]+d
            if distance[adj]>cost:
                distance[adj]=cost
                heappush(q,(cost,adj))
    return distance[1:]

if __name__=="__main__":
    v, e, start = map(int, input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        f,t,d=map(int,input().split())
        graph[f].append((t,d))
    
    i_to_x=dijstra(graph, start)
    x_to_i=[i_to_x[i-1]+dijstra(graph,i)[start-1] for i in range(1,v+1)]
    print(max(x_to_i))