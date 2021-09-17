from collections import deque

def solution(n,m,graph):
    return bfs(0,0, n,m, graph)
    

def bfs(x, y, n,m, graph):
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    queue=deque([(x,y)])
    while queue:
        curx, cury=queue.popleft()
        for i in range(4):
            x, y = curx+dx[i], cury+dy[i]
            if 0<=x<n and 0<=y<m and graph[x][y]==1:
                graph[x][y]=graph[curx][cury]+1
                queue.append((x,y))
    return graph[n-1][m-1]

if __name__=="__main__":
    n,m=map(int, input().split())
    graph=[list(map(int, list(input()))) for _ in range(n)]
    print(solution(n,m,graph))