import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
parent=[i for i in range(n+1)]

def union_parent(parent, a,b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]
     

for _ in range(m):
    check, a, b = map(int, sys.stdin.readline().split())
    if check:
        print('yes') if find_parent(parent, a)==find_parent(parent, b) else print('no')
    else:
        union_parent(parent,a,b)