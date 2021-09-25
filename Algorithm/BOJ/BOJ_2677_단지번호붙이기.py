#!/usr/bin/env python
# coding: utf-8
'''
Bfs deque 자료구조 이용해 풀었음 
Map 이중포문 돌면서 모든 인덱스 탐색 중 값이 1이고 
이미 아파트 단지 안에 들어간 인덱스 제외 bfs 탐색 시작 
이미 아파트 단지 안에 들어간 인덱스, bfs 내부 visit 은 다 딕셔너리(해시) 로 구현해 시간 단축
'''

from collections import deque

def neighbor(cur_pos, N): # cur_pos=[x,y] 현재 집위치
    x=cur_pos[0]; y=cur_pos[1];
    
    if( 0<x and x<N-1 and 0<y and y<N-1):
        return [[x,y-1], [x,y+1], [x-1,y], [x+1,y]]
    else:
        if(x==0):
            if(y==0):
                return [[x,y+1], [x+1,y]]
            elif(y==N-1):
                return [[x,y-1], [x+1,y]]
            else:
                return[[x, y-1], [x+1,y], [x,y+1]]
        elif(x==N-1):
            if(y==0):
                return [[x-1,y],[x,y+1]]
            elif(y==N-1):
                return [[x,y-1], [x-1,y]]
            else:
                return [[x,y-1], [x-1,y], [x,y+1]]
        elif(y==0):
            return [[x, y+1], [x-1,y], [x+1,y]]
        elif(y==N-1):
            return[[x,y-1],[x-1,y],[x+1,y]]


def find_apartment(Map, cur_pos, N):
    global already_in_apartment
    condition=False
    house=0
    visit={}
    q=deque([cur_pos])
    
    while len(q) > 0:
        ngh_x, ngh_y =q.popleft()
        condition=False
        
        if(ngh_x not in visit.keys()):
            visit[ngh_x]=[ngh_y]
            condition=True
                    
        elif(ngh_y not in visit[ngh_x]):
            visit[ngh_x].append(ngh_y)
            condition=True
            
        if(condition):   
            neighbors=neighbor([ngh_x, ngh_y], N)
            for x,y in neighbors:
                if(Map[x][y]==1):
                    q.append([x,y]) 
            house+=1
    
    for x in visit.keys():
        if(x not in already_in_apartment.keys()):
            already_in_apartment[x]=visit[x]
        else:
            already_in_apartment[x].extend(visit[x])
            already_in_apartment[x]=list(set(already_in_apartment[x]))
            
    return house


if __name__ == "__main__":
    N=int(input())
    Map=[list(map(int, input())) for _ in range(N)]
    result=[]
    
    global already_in_apartment
    already_in_apartment={}
    
    for pos_x in range(N):
        for pos_y in range(N):
            condition=False
            if(Map[pos_x][pos_y]==1):
                if(pos_x not in already_in_apartment.keys()):
                    condition=True
                elif(pos_y not in already_in_apartment[pos_x]):
                    condition=True
                if(condition):
                    house=find_apartment(Map, [pos_x, pos_y], N)
                    result.append(house)
    result.sort()
    print(len(result))
    for cnt in result:
        print(cnt)

