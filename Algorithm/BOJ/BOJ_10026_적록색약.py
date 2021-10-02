from collections import deque
def get_area(i,j, flag):
    visited=[[False]*n for _ in range(n)]

    def bfs(i,j, flag):
        dx,dy=[1,-1,0,0],[0,0,1,-1]
        q=deque([(i,j)])
        visited[i][j]=True
        while q:
            x,y=q.popleft()
            for i in range(4):
                mx,my=x+dx[i],y+dy[i]
                if 0<=mx<n and 0<=my<n and graph[mx][my] in flag and not visited[mx][my]:
                    visited[mx][my]=True
                    q.append((mx,my))
    count=0
    if flag==1:
        for alpha in ('R','G','B'):
            for r in range(n):
                for c in range(n):
                    if graph[r][c]==alpha and not visited[r][c]:
                        bfs(r,c,alpha)
                        count+=1
    else:
        for alpha in ('RG','B'):
            for r in range(n):
                for c in range(n):
                    if graph[r][c] in alpha and not visited[r][c]:
                        bfs(r,c,alpha)
                        count+=1
    return count

n=int(input())
graph=[list(input()) for _ in range(n)]
print(get_area(0,0,1), get_area(0,0,2), sep=' ')