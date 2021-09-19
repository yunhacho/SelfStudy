from collections import deque

def bfs(graph, x, y, s, n):
    dx=[-1,1,0,0]; dy=[0,0,1,-1]
    queue=deque(sorted([(graph[i][j],i,j) for i in range(n) for j in range(n) if graph[i][j]!=0]))
    
    count=0
    while queue:
        if count==s: break
        for _ in range(len(queue)):
            virus, curx, cury=queue.popleft()
            for i in range(4):
                nx, ny = curx+dx[i], cury+dy[i]
                if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                    graph[nx][ny]=virus
                    queue.append([virus,nx,ny])
        count+=1
    return graph[x-1][y-1]
            
if __name__=="__main__":
    n, k = map(int, input().split())
    graph=[list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    print(bfs(graph, x, y, s, n))
