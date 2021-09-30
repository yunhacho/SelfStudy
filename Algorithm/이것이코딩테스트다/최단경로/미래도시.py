from heapq import heappush, heappop
def Floyd(graph, x, k):
    for i in range(1, len(graph)):
        for a in range(1,len(graph)):
            for b in range(1,len(graph)):
                graph[a][b]=min(graph[a][b], graph[a][i]+graph[i][b])
                graph[b][a]=min(graph[a][b], graph[a][i]+graph[i][b])

    return graph[1][k]+graph[k][x] if graph[1][k]+graph[k][x] < int(1e9) else -1

def dijkstra(graph, x):
    q=[]
    distance=[int(1e9)]*len(graph)
    distance[x]=0
    heappush(q,(0,x))
    while q:
        dist_of_vertex, vertex=heappop(q)
        if dist_of_vertex > distance[vertex]: continue
        for adj in graph[vertex]:
            cost=distance[vertex]+1
            if cost < distance[adj]:
                distance[adj]=cost
                heappush(q, (cost, adj))
    return distance

def dijstra_solution(graph, x, k):
    dijk_from_start=dijkstra(graph,1)
    dijk_from_k=dijkstra(graph,k)
    return dijk_from_start[k]+dijk_from_k[x] if dijk_from_start[k]+dijk_from_k[x] < int(1e9) else -1

if __name__=="__main__":
    v, e = map(int, input().split())
    graph=[[int(1e9)]*(v+1) for _ in range(v+1)]
    dijkgraph=[[] for _ in range((v+1))]

    for i in range(v+1): graph[i][i]=0
    for i in range(e):
        a,b=map(int, input().split())
        graph[a][b]=1
        graph[b][a]=1

        dijkgraph[a].append(b)
        dijkgraph[b].append(a)

    x, k = map(int, input().split())
    print(Floyd(graph,x,k))
    print(dijstra_solution(dijkgraph, x, k))