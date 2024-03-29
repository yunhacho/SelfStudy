N, M = map(int, input().split())
graph=[list(map(int, list(input()))) for _ in range(N)]

def dfs(x,y):
    if 0<=x<N and 0<=y<M:
        if graph[x][y]==0:
            graph[x][y]=1
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return True
    return False

count=0
for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            count+=1
print(count)

