import sys
import heapq
from collections import deque
input=sys.stdin.readline

def get_shortest_path(map_of_passenger, arrive_flag=False, arrive_r=None, arrive_c=None):
    shortest_path=[]; count=number_of_passenger
    map_of_path=[[0]*n for _ in range(n)]
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    queue=deque([(driver_r,driver_c)])
    map_of_path[driver_r][driver_c]=1
    while queue:
        cur_r,cur_c=queue.popleft()
        if arrive_flag:
            if cur_r==arrive_r and cur_c==arrive_c:
                return (map_of_path[cur_r][cur_c]-1,cur_r,cur_c,0) if map_of_path[cur_r][cur_c]-1<=fuel else []
        elif map_of_passenger[cur_r][cur_c]!=0:
            heapq.heappush(shortest_path, (map_of_path[cur_r][cur_c]-1,cur_r,cur_c, map_of_passenger[cur_r][cur_c]))
            count-=1
            if count==0: break
        for x,y in zip(dx,dy):
            mx,my=cur_r+x,cur_c+y
            if CanGo(mx,my) and map_of_path[mx][my]==0:
                map_of_path[mx][my]=map_of_path[cur_r][cur_c]+1
                queue.append((mx,my))
    if shortest_path:
            shortest=heapq.heappop(shortest_path)
    else: return []
    return shortest if shortest[0]<=fuel else []

CanGo=lambda r,c: 0<=r<n and 0<=c<n and maps[r][c]==0

n,m,fuel=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]

driver_r,driver_c=map(int,input().split())
driver_r-=1; driver_c-=1

map_of_from_passenger=[[0]*n for _ in range(n)]
map_of_to_passenger=[None]
for i in range(m):
    from_r,from_c,to_r,to_c=map(int,input().split())
    map_of_from_passenger[from_r-1][from_c-1]=i+1
    map_of_to_passenger.append((to_r-1,to_c-1))

number_of_passenger=m
for _ in range(m):
    # driver to passenger
    passenger=get_shortest_path(map_of_from_passenger)
    if not passenger: fuel=-1; break
    else:
        d_to_p_dist, driver_r, driver_c, p_n = passenger
        fuel-=d_to_p_dist
        map_of_from_passenger[driver_r][driver_c]=0

        #passenger to 목적지
        passenger=get_shortest_path(map_of_to_passenger,True, map_of_to_passenger[p_n][0],map_of_to_passenger[p_n][1])
        if not passenger: fuel=-1; break
        else:
            p_to_arrive_dist,driver_r, driver_c,_=passenger
            fuel+=p_to_arrive_dist
    number_of_passenger-=1

print(fuel)
