import sys

def dfs(x,y,cnt):
    global count
    dx,dy=[1,-1,0,0], [0,0,1,-1]
    count=max(count,cnt)
    for i in range(4):
        mx, my = x+dx[i], y+dy[i]
        if 0<=mx<r and 0<=my<c and not alphabet[graph[mx][my]]:
            alphabet[graph[mx][my]]=True
            dfs(mx,my,cnt+1)
            alphabet[graph[mx][my]]=False
        

r,c=map(int,sys.stdin.readline().split())
alphabet=[False]*26
graph=[list(map(lambda x: ord(x)-ord('A'), sys.stdin.readline())) for _ in range(r)]

count=1
alphabet[graph[0][0]]=True
dfs(0,0,count)
print(count)