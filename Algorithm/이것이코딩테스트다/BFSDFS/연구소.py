# 삼성전자SW역량테스트, BOJ 14502
from itertools import product, combinations
from collections import deque
import copy

def get_pos(graph):
    zero=[]; virus=[]
    for c in product(range(len(graph)), range(len(graph[0]))):
        if graph[c[0]][c[1]]==0: zero.append(c)
        elif graph[c[0]][c[1]]==2: virus.append(c)
    return zero, virus

def bfs(origin, c, initvirus):
    maps=copy.deepcopy(origin)
    for x,y in c: maps[x][y]=1
    dx=[-1,1,0,0]; dy=[0,0,1,-1]
    queue=deque()
    queue.extend(initvirus)

    while queue:
        curx, cury=queue.popleft()
        for i in range(4):
            x,y=curx+dx[i], cury+dy[i]
            if 0<=x<len(maps) and 0<=y<len(maps[0]) and maps[x][y]==0:
                maps[x][y]=2
                queue.append((x,y))

    return get_score(maps)

def get_score(graph):
    cnt=0
    for row in graph:
        for col in row: 
            if col==0:
                cnt+=1
    return cnt

def solutions(graph):
    result=-1
    zero, initvirus = get_pos(graph)
    for c in combinations(zero,3):
        result=max(result,bfs(graph, c, initvirus))
    return result

if __name__=="__main__":
    n, m = map(int, input().split())
    graph=[list(map(int, input().split())) for _ in range(n)]
    print(solutions(graph))