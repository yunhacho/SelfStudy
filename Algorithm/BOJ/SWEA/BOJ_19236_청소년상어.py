import sys
import heapq
from copy import deepcopy
input=sys.stdin.readline

def fish_move(maps):
    direction=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    heap=make_heap(maps)
    check=[False]*(17)
    while heap:
        num,dir,r,c = heapq.heappop(heap)
        if not check[num] and maps[r][c][0]==num:
            for d in range(dir, dir+9):
                mx,my=r+direction[d%8][0],c+direction[d%8][1]
                if 0<=mx<n and 0<=my<n and maps[mx][my][0]>=0:
                    maps[mx][my], maps[r][c] = [num, d%8], maps[mx][my][:]
                    if maps[mx][my][0] < maps[r][c][0]:
                        heapq.heappush(heap, maps[r][c][:]+[r,c])
                    check[num]=True
                    break
    return maps

def make_heap(maps):
    queue=[]
    for i in range(n):
        for j in range(n):
            if maps[i][j][0]>0: 
                heapq.heappush(queue, maps[i][j][:]+[i,j])
    return queue

def where_shark_to_move(maps, shark_x, shark_y, shark_dir):
    direction=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    candidates=[]
    for i in range(1,4):
        mx=shark_x+(i*direction[shark_dir][0])
        my=shark_y+(i*direction[shark_dir][1])
        if 0<=mx<n and 0<=my<n:
            if maps[mx][my][0]>0:
                candidates.append([mx,my])
    return candidates

def dfs(maps,shark_x, shark_y, shark_sum, shark_dir):
    global max_total
    maps=fish_move(maps)
    candidates=where_shark_to_move(maps,shark_x, shark_y, shark_dir)
    if not candidates:
        max_total=max(max_total, shark_sum)
        return
    for cx,cy in candidates:
        origin_num, origin_dir=maps[cx][cy]
        maps[cx][cy]=[-1,origin_dir]
        maps[shark_x][shark_y]=[0,0]
        dfs(deepcopy(maps) ,cx,cy,shark_sum+origin_num, origin_dir)
        maps[cx][cy]=[origin_num, origin_dir]
        maps[shark_x][shark_y]=[-1,shark_dir]

n=4
init_map=[]
for _ in range(n):
    line=list(map(int, input().split()))
    row=[[line[i], line[i+1]-1] for i in range(0,(2*n)-1,2)]
    init_map.append(row)

shark_x, shark_y, shark_sum, shark_dir = 0,0,init_map[0][0][0], init_map[0][0][1]
max_total=0
init_map[0][0]=[-1,-1]

dfs(init_map, shark_x, shark_y, shark_sum, shark_dir)
print(max_total)