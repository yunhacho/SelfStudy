from collections import deque
graph=dict()
graph['A']=['B','C']
graph['B']=['A','D']
graph['C']=['A','G','H','I']
graph['D']=['B','E','F']
graph['E']=['D']
graph['F']=['D']
graph['G']=['C']
graph['H']=['C']
graph['I']=['C']
graph['J']=['I']

def bfs(graph, root):
    visited=[]
    needtovisit=deque()
    needtovisit.append(root)

    while needtovisit:
        node=needtovisit.popleft()
        if node not in visited:
            needtovisit.extend(graph[node])
            visited.append(node)
    return visited

def dfs(graph, root):
    visited=[]
    needtovisit=[]
    needtovisit.append(root)

    while needtovisit:
        node=needtovisit.pop()
        if node not in visited:
            visited.append(node)
            needtovisit.extend(graph[node])
    return visited

print(bfs(graph, 'A'))
print(dfs(graph, 'A'))
