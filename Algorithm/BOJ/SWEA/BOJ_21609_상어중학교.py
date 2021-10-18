import sys
from collections import deque
input=sys.stdin.readline

def get_biggest_group():

    def bfs(row,col,color):
        block=[]
        cnt_of_rainbow=0
        min_r, min_c=n-1,n-1
        dx, dy = [-1,1,0,0], [0,0,-1,1]
        queue=deque([(row,col)])
        visited[row][col]=True
        while queue:
            r,c=queue.popleft()
            for x,y in zip(dx,dy):
                mr,mc=r+x,c+y
                if 0<=mr<n and 0<=mc<n and not visited[mr][mc]:
                    if maps[mr][mc]==color or maps[mr][mc]==0:
                        queue.append((mr,mc))
                        visited[mr][mc]=True
            if maps[r][c]==0: cnt_of_rainbow+=1
            else: 
                if min_r>=r:
                    min_r, min_c= r, min(min_c, c)
            block.append((r,c))
        return len(block), cnt_of_rainbow, min_r, min_c,block

    groups=[]
    visited=[[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and maps[i][j]>0:
                size, cnt_of_rainbow, min_r, min_c, block=bfs(i,j,maps[i][j])
                if size<2:
                    for r,c in block: visited[r][c]=False
                else: 
                    for r,c in block:
                        if maps[r][c]==0: visited[r][c]=False
                    groups.append([size, cnt_of_rainbow, min_r, min_c, block])

    return sorted(groups, key=lambda x: (-x[0], -x[1], -x[2], -x[3]))[0][4] if groups else []

def remove_and_get_score(group):
    global total
    for r,c in group: maps[r][c]=-2
    total+=pow(len(group),2)
    return 

def rotate_map():
    global maps
    new_map=[item for item in zip(*maps)]   
    maps=[list(new_map[i][:]) for i in range(n-1,-1,-1)]

def get_gravity():
    for k in range(n):
        for i in range(n-2,-1,-1):
            if maps[i][k]>-1:
                prev_r, prev_c = i,k
                for j in range(i+1, n):
                    if maps[j][k]==-2:
                        maps[j][k]=maps[prev_r][prev_c]
                        maps[prev_r][prev_c]=-2
                        prev_r, prev_c = j, k
                    else: break
    return

n,m=map(int, input().split())
maps=[list(map(int, input().split())) for _ in range(n)]
total=0

while True:
    group=get_biggest_group()
    if not group: break
    remove_and_get_score(group)
    get_gravity()
    rotate_map()
    get_gravity()

print(total)
