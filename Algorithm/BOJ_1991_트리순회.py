import sys
# inorder traversal
def inorder(data):
    if data=='.': return
    inorder(graph[data][0])
    print(data,end='')
    inorder(graph[data][1])

# preorder traversal
def preorder(data):
    if data=='.': return
    print(data, end='')
    preorder(graph[data][0])
    preorder(graph[data][1])

# postorder traversal
def postorder(data):
    if data=='.': return
    postorder(graph[data][0])
    postorder(graph[data][1])
    print(data, end='')

if __name__=="__main__":
    graph={}
    for _ in range(int(input())):
        root, left, right = sys.stdin.readline().split()
        graph[root]=(left, right)
    preorder('A'); print()
    inorder('A'); print()
    postorder('A')
