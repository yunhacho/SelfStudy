#!/usr/bin/env python
# coding: utf-8

if __name__=="__main__":
    N=int(input())
    connected_num=int(input())
    
    graph={}
    for _ in range(connected_num):
        v1, v2=map(int, input().split())
        if(v1 in graph.keys()):
            graph[v1].append(v2)
        else:
            graph[v1]=[v2]
        
        if(v2 in graph.keys()):
            graph[v2].append(v1)
        else:
            graph[v2]=[v1]
            
    print(dfs(graph, 1))


def dfs(graph, start_node):
    infected=-1
    visit={}; stack=[start_node];
    
    while stack:
        node=stack.pop()
        if(node not in visit.keys()):
            visit[node]=True
            stack.extend(graph[node])
            infected+=1
    return infected

