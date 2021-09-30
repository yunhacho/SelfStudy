# 모든 노드에서 모든 노드로 최단 거리

def Floyd(graph):
    for k in range(1,len(graph)):
        for a in range(1, len(graph)):
            for b in range(1,len(graph)):
                graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
    return [g[1:] for g in graph[1:]]

if __name__=="__main__":
    v, e = map(int, input().split())
    graph=[[int(1e9)]*(v+1) for _ in range(v+1)]

    for _ in range(e):
        a,b,d=map(int, input().split())
        graph[a][b]=d

    for i in range(v+1):
        graph[i][i]=0

    graph=Floyd(graph)

    print(*graph, sep='\n')

