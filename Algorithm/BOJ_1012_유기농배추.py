#!/usr/bin/env python
# coding: utf-8

def neighbor(N,M,pos_x, pos_y):
    if(0<pos_x and pos_x<M-1 and 0<pos_y and pos_y<N-1):
        return [[pos_x,pos_y-1],[pos_x-1,pos_y],[pos_x,pos_y+1],[pos_x+1,pos_y]]
    elif(pos_x==0):
        if(pos_y==0):
            return[[pos_x,pos_y+1],[pos_x+1,pos_y]]
        elif(pos_y==N-1):
            return[[pos_x,pos_y-1],[pos_x+1,pos_y]]
        else:
            return[[pos_x,pos_y-1],[pos_x,pos_y+1],[pos_x+1,pos_y]]
    elif(pos_x==M-1):
        if(pos_y==0):
            return [[pos_x-1,pos_y],[pos_x,pos_y+1]]
        elif(pos_y==N-1):
            return [[pos_x,pos_y-1],[pos_x-1,pos_y]]
        else:
            return [[pos_x-1,pos_y],[pos_x,pos_y-1],[pos_x,pos_y+1]]
    elif(pos_y==0):
        return [[pos_x-1,pos_y],[pos_x,pos_y+1],[pos_x+1,pos_y]]
    elif(pos_y==N-1):
        return [[pos_x-1,pos_y],[pos_x,pos_y-1],[pos_x+1,pos_y]]

def is_in_graph(graph, x, y): #graph 는 딕셔너리
    if x not in graph.keys(): # graph key에 x 가 없는 경우
        return [False, False]
    elif y not in graph[x]: # graph key에 x가 있지만 graph[x]에 y가 없는 경우
        return [False, True]
    else:
        return [True, True] # graph[x]에 y가 있는 경우

def bfs(cabmap, start_cabbage, M,N): # Y축 길이, X축 길이
    visit={}
    stack=[start_cabbage]
    
    while stack:
        pos_x, pos_y=stack.pop()
        in_visit, in_visit_key= is_in_graph(visit ,pos_x,pos_y)
        
        if not in_visit:
            if in_visit_key:
                visit[pos_x].append(pos_y)
            else:
                visit[pos_x]=[pos_y]
                
            neighbors=neighbor(M, N,pos_x,pos_y)
            for ngh_x, ngh_y in neighbors:
                in_cabmap, in_map_key=is_in_graph(cabmap, ngh_x, ngh_y)
                if in_cabmap:
                    stack.append([ngh_x, ngh_y])

    return visit

if __name__=="__main__":
    worms=[]
    for _ in range(int(input())):
        cabbage_map={}
        worm=0
        M, N, num_of_cabbage=map(int, input().split())
        
        for cab in range(num_of_cabbage):
            pos_y, pos_x=map(int, input().split())
            
            if pos_x in cabbage_map.keys():
                cabbage_map[pos_x].append(pos_y)
            else:
                cabbage_map[pos_x]=[pos_y]
                
        while cabbage_map:
            pos_x=list(cabbage_map.keys())[0]
            pos_y=cabbage_map[pos_x][0]
            visit=bfs(cabbage_map, [pos_x, pos_y],M, N)

            if visit:
                worm+=1
                for x in visit.keys():
                    remainder=list(set(cabbage_map[x])-set(visit[x]))

                    if remainder:
                        cabbage_map[x]=remainder
                    else:
                        del cabbage_map[x]
                        
        worms.append(worm)
    
    for w in worms:
        print(w)

