import sys
from collections import deque
import heapq
input=sys.stdin.readline

n=int(input())
maps=[list(map(int,input().split())) for _ in range(n)]
br,bc=0,0

shark=False
for i in range(n):
    for j in range(n):
        if maps[i][j]==9: 
            br,bc=i,j
            shark=True
            break
    if shark: break

def find_fish_to_eat(br,bc,babysize):
    candidates=[]
    queue=deque()
    visited=[[False]*n for _ in range(n)]
    visited[br][bc]=True
    dx,dy=[1,-1,0,0],[0,0,-1,1]
    queue.append([br,bc,0])
    while queue:
        cur_r,cur_c,time=queue.popleft()
        for x,y in zip(dx,dy):
            mx,my=cur_r+x, cur_c+y
            if 0<=mx<n and 0<=my<n and not visited[mx][my]:
                visited[mx][my]=True
                if maps[mx][my]==babysize or maps[mx][my]==0:
                    queue.append([mx,my,time+1])
                elif maps[mx][my]<babysize:
                    heapq.heappush(candidates,(time+1,mx,my,maps[mx][my]))

    return heapq.heappop(candidates) if candidates else None

time=0
baby_size=2
count=0
while True:
    maps[br][bc]=0
    candidate=find_fish_to_eat(br,bc,baby_size)
    if candidate is None:
        break
    time2eat,br,bc,size=candidate
    count+=1
    if count==baby_size:
        baby_size+=1
        count=0
    time+=time2eat
print(time)