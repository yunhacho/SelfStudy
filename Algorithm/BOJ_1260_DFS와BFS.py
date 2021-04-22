#!/usr/bin/env python
# coding: utf-8

import sys
from collections import deque

def bfs(graph, start_node):
    visit={}
    result=[]
    
    if(start_node not in graph.keys()):
        print(start_node, end=' ')
        return
    q=deque([start_node])
    
    while len(q) >0:
        node=q.popleft()
        if node not in visit.keys():
            print(node, end=' ')
            visit[node]=True
            graph[node].sort()
            q.extend(graph[node])
    return

def dfs(graph, start_node):
    visit={}
    stack=[]
    result=[]
    
    if(start_node not in graph.keys()):
        print(start_node, end=' ')
        return
    stack.append(start_node)
    
    while stack:
        node=stack.pop()
        if node not in visit.keys():
            print(node, end=' ')
            visit[node]=True
            graph[node].sort(reverse=True)
            stack.extend(graph[node])
    return

if __name__=="__main__":
    graph={}

    N, M, V=map(int, input().split())

    for _ in range(M):
        v1, v2=map(int, input().split())

        if v1 in graph.keys():
            graph[v1].append(v2)
        else:
            graph[v1]=[v2]

        if v2 in graph.keys():
            graph[v2].append(v1)
        else:
            graph[v2]=[v1]
    
    dfs(graph, V)
    print()
    bfs(graph, V)

